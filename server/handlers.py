# -*- coding:utf-8 -*-

import time
import tornado.web


    
def processXml(xml):
    xdict = toDict(xml)
    if xdict['MsgType'] == 'event':
        if xdict['Event'] == 'subscribe':
            # 返回欢迎订阅，与帮助信息
            text = u"欢迎订阅Bus通"
            text = '\n'.join([text, help_message])
        elif xdict['Event'] == 'unsubscribe':
            #db = SaeDb(xdict['FromUserName'])
            #db.delete()
            return None
    elif xdict['MsgType'] == 'text':
        t = xdict['Content']
        text = t
    	print xdict['FromUserName'], 'to', xdict['ToUserName'], 'says', text.encode('U8', 'ignore')
        if text.lower() == 'help':
            text = help_message
    else:
        # 返回帮助信息
        text = help_message
    kw = dict.fromkeys(['ToUserName', 'FromUserName', 'CreateTime', 'Content'])
    kw['ToUserName'] = xdict['FromUserName']
    kw['FromUserName'] = xdict['ToUserName']
    kw['CreateTime'] = int(time.time())
    kw['Content'] = text
    return toXml(kw)
    
