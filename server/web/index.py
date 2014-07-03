#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
index.py
Author: yupbank
Email:  yupbank@gmail.com

Created on
2014-07-03
'''
from .base import BaseHandler


class IndexHandler(BaseHandler):
    url_path = '/'

    def get(self):
        self.write('<h1>welcome</h1><br/>follow <img src="http://ww1.sinaimg.cn/large/5e0eccddgw1ehxkdy776wj20zk0zktct.jpg"/>')
