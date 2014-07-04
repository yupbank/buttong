#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
settings.py
Author: yupbank
Email:  yupbank@gmail.com

Created on
2014-07-03
'''

setting = {
        'debug': True
        }

API_BASE = 'http://hkbus.axon-labs.com/api'
SUGGETION = '/search/suggestions?q=%s'
UUID = '888'
TOKEN = 'bustong2014' # 微信公众号 TOKEN

welcome_message = u"欢迎订阅Bus通"

help_message = u'''使用指南:
0 提示: help
1 查询bus: q:xx
2 查询外卖: to be done... 
q 以外只能重复你的消息
'''

XMLTEMPLATE = """<xml>
<ToUserName><![CDATA[$ToUserName]]></ToUserName>
<FromUserName><![CDATA[$FromUserName]]></FromUserName>
<CreateTime>$CreateTime</CreateTime>
<MsgType><![CDATA[text]]></MsgType>
<Content><![CDATA[$Content]]></Content>
</xml>"""
