#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
app.py
Author: yupbank
Email:  yupbank@gmail.com

Created on
2014-07-03
'''
import tornado.web
from apis import api_handlers
from web import web_handlers
from settings import setting

handlers = []
handlers.extend(api_handlers)
handlers.extend(web_handlers)
application = tornado.web.Application(handlers, **setting)

if __name__ == '__main__':
    import tornado.ioloop
    import tornado.httpserver
    server = tornado.httpserver.HTTPServer(application)
    server.listen(8086)
    print 'running on 8086'
    tornado.ioloop.IOLoop.instance().start()
