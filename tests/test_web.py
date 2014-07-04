#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
test_web.py
Author: yupbank
Email:  yupbank@gmail.com

Created on
2014-07-03
'''
from .framework import HTTPClientMixin
from tornado.testing import AsyncHTTPTestCase
import tornado
from ..conftest import application
import pytest
from urllib import urlencode


t_data = None
t_xml = None
def test_data(data_fortest):
    global t_data
    t_data = data_fortest

def test_xml(xml):
    global t_xml
    t_xml = xml

class ApplicationTestCase(AsyncHTTPTestCase, HTTPClientMixin):
    def get_new_ioloop(self):
        print 'vistied....'
        return tornado.ioloop.IOLoop.instance()

    def get_app(self):
        return  application

    def test_homepage(self):
        url = '/'
        response = self.get(url)
        self.assertTrue('welcome' in response.body)
    
    def test_get_webchat(self):
        echo_strs = ['text', 'event', u'中文恩']
        url = '/wechat'
        for echo in echo_strs:
            echo = echo.encode('U8')
            data = t_data
            data.update({'echostr':echo})
            response = self.get(url, data=data)
            self.assertTrue(echo in response.body)

    def test_post_wechat(self):
        data = t_data
        url = '/wechat'
        if isinstance(data, dict):
            data = urlencode(data)
        if '?' in url:
            url += '&amp;%s' % data
        else:
            url += '?%s' % data
        response = self.post(url, t_xml)
        if 'q:' in t_xml:
            self.assertTrue('company' in response.body)
        if not 'unsubscribe' in t_xml and 'q:' not in t_xml:
            self.assertTrue('how' in response.body or 'help' in response.body)
    
