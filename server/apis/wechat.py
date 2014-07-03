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
        signature = self.get_argument('signature')
        timestamp = self.get_argument('timestamp')
        nonce =  self.get_argument('nonce')
        echo_str = self.get_argument('echostr')
        if valid(signature, timestamp, nonce):
            self.write(echo_str)

    @tornado.web.asynchronous
    def post(self):
        signature = self.get_argument('signature')
        timestamp = self.get_argument('timestamp')
        nonce =  self.get_argument('nonce')
        data = self.request.body
        message = toDict(data)
        message = return_back(message, self.callback)
        if message:
            return self.finish(message)

    def callback(self, xdict, message):
        form_message(xdict, message)
        return self.finish(message)
