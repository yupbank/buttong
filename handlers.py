# -*- coding:utf-8 -*-

import time
from jsquery import query, queryAny
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
    
def processXml(xml):

    help = u'''使用指南:
1 查询净值 000001
2 基金订阅 a000001
3 查询订阅 c
4 取消订阅 r000001
5 <a href="https://me.alipay.com/zhu327">点击赞助</a>
'''

    xdict = toDict(xml)
    if xdict['MsgType'] == 'event':
        if xdict['Event'] == 'subscribe':
            # 返回欢迎订阅，与帮助信息
            text = u"欢迎订阅基金查查"
            text = '\n'.join([text, help])
        elif xdict['Event'] == 'unsubscribe':
            #db = SaeDb(xdict['FromUserName'])
            #db.delete()
            return None
    elif xdict['MsgType'] == 'text':
        t = xdict['Content']
        print t
        text = t
    else:
        # 返回帮助信息
        text = help
    kw = dict.fromkeys(['ToUserName', 'FromUserName', 'CreateTime', 'Content'])
    kw['ToUserName'] = xdict['FromUserName']
    kw['FromUserName'] = xdict['ToUserName']
    kw['CreateTime'] = int(time.time())
    kw['Content'] = text
    return toXml(kw)
    
