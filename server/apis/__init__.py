#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
__init__.py
Author: yupbank
Email:  yupbank@gmail.com

Created on
2014-07-03
'''
from .base import BaseHandler
from .wechat import WechatHandler

api_handlers = []

for k, v in dict(globals()).iteritems():
    if type(v) is type and issubclass(v, BaseHandler) and \
            v is not BaseHandler:
        api_handlers.append((getattr(v, 'url_path'), v))
