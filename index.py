# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web
import handlers
            
class WechatHandler(tornado.web.RequestHandler):
    def get(self):
        try:
            if handlers.valid(self.get_argument('signature'),
                        self.get_argument('timestamp'),
                        self.get_argument('nonce')):
                self.write(self.get_argument('echostr'))
        except tornado.web.HTTPError:
            self.write('')
    
    def post(self):
        try:
            if handlers.valid(self.get_argument('signature'),
                        self.get_argument('timestamp'),
                        self.get_argument('nonce')):
                data = handlers.processXml(self.request.body)
                self.set_header("Content-Type", "application/xml; charset=UTF-8")
                self.write(data)
        except tornado.web.HTTPError:
            self.write('')

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('<h1>welcome</h1><br/>follow <img src="http://ww1.sinaimg.cn/large/5e0eccddgw1ehxkdy776wj20zk0zktct.jpg"/>')

application = tornado.web.Application([
    (r"/wechat", WechatHandler),
    (r"/i", IndexHandler),
    (r"/", IndexHandler),
    #(r"/", tornado.web.RedirectHandler, dict(url="http://yupbank.org")),
], debug=True)

if __name__ == "__main__":
    application.listen(8086)
    print '127.0.0.1:8086'
    tornado.ioloop.IOLoop.instance().start()
