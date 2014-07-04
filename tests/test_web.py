#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
test_web.py
Author: yupbank
Email:  yupbank@gmail.com

Created on
2014-07-03
'''
from tornado.testing import AsyncHTTPTestCase
from ..conftest import application

class ApplicationTestCase(AsyncHTTPTestCase):
    def get_app(self):
        return  application

    def test_homepage(self):
        url = '/'
        self.http_client.fetch(self.get_url(url), self.stop)
        response = self.wait()
        self.assertTrue('welcome' in response.body)
