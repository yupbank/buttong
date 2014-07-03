# -*- coding:utf-8 -*-

import time
from wxml import toDict, toXml
#from saedb import SaeDb
from hashlib import sha1

TOKEN = 'bustong2014' # 微信公众号 TOKEN

def valid(signature, timestamp, nonce):
        li = []

        li.append(TOKEN)
        li.append(nonce)
        li.append(timestamp)

        li.sort()

        tmpWord = ''.join(li)
        tmpWord = sha1(tmpWord).hexdigest()


        if tmpWord == signature:
            return True
        else:
            return False
    
help_message = u'''使用指南:
0 help: for manual
1 查询bus: busxx
2 查询外卖 wamaixx
其实现在只能重复你的消息
'''
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
    
