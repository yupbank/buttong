#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
wechat.py
Author: yupbank
Email:  yupbank@gmail.com

Created on
2014-07-03
'''

from .base import ApiHandler
from util import valid, toDict, form_message
from ctrl import return_back
import tornado.web

class WechatHandler(ApiHandler):
    url_path = '/wechat'

    def get(self):
        signature = self.get_argument('signature', None)
        timestamp = self.get_argument('timestamp', None)
        nonce =  self.get_argument('nonce', None)
        echo_str = self.get_argument('echostr', None)
        if valid(signature, timestamp, nonce):
            self.finish(echo_str or ' ')

    @tornado.web.asynchronous
    def post(self):
        signature = self.get_argument('signature')
        timestamp = self.get_argument('timestamp')
        nonce =  self.get_argument('nonce')
        data = self.request.body
        if valid(signature, timestamp, nonce):
            message = toDict(data)
            message = return_back(message, self.callback)
            if message:
                return self.finish(message)

    def callback(self, xdict, message):
        form_message(xdict, message)
        return self.finish(message)
