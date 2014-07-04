#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
wechat.py
Author: yupbank
Email:  yupbank@gmail.com

Created on
2014-07-03
'''
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from .base import ApiHandler
from util import valid, toDict, form_message
from ctrl import return_back, is_query
from search import suggestion
from functools import partial
import tornado.web
import json

class WechatHandler(ApiHandler):
    url_path = '/wechat'

    def get(self):
        signature = self.get_argument('signature', None)
        timestamp = self.get_argument('timestamp', None)
        nonce =  self.get_argument('nonce', None)
        echo_str = self.get_argument('echostr', None)
        if valid(signature, timestamp, nonce):
            print self.request.body
            return self.finish(echo_str or ' ')

    @tornado.web.asynchronous
    def post(self):
        signature = self.get_argument('signature')
        timestamp = self.get_argument('timestamp')
        nonce =  self.get_argument('nonce')
        data = self.request.body
        if valid(signature, timestamp, nonce):
            message = toDict(data)
            message, xdict = return_back(message)
            if message and not is_query(message):
                return self.finish(message)
            elif is_query(message):
                suggestion(message[2:].strip(), partial(self.callback, xdict))
            else:
                return self.finish('not valid')

        else:
            return self.finish('not valid')

    def callback(self, xdict, message):
        new_message = form_message(xdict, json.loads(message.body)['data'][0]['suggestion'])
        return self.finish(new_message)
