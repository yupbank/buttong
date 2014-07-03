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


