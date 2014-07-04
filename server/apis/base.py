#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
base.py
Author: yupbank
Email:  yupbank@gmail.com

Created on
2014-07-03
'''
import tornado.web


class BaseHandler(tornado.web.RequestHandler):
    @property
    def url_path(self):
        raise NotImplementedError


class ApiHandler(BaseHandler):
    def write(self, data):
        self.set_header("Content-Type", "application/xml; charset=UTF-8")
        return super(ApiHandler, self).write(data)
