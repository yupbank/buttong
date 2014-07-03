#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
conftest.py
Author: yupbank
Email:  yupbank@gmail.com

Created on
2014-07-03
'''
import time

import pytest

from wxml import toDict, toXml

@pytest.fixture(scope="module")
def xml(request):
    s = """<xml>
    <ToUserName><![CDATA[rec]]></ToUserName>
    <FromUserName><![CDATA[sender]]></FromUserName>
    <CreateTime>1232322</CreateTime>
    <MsgType><![CDATA[text]]></MsgType>
    <Content><![CDATA[how are you]]></Content>
    </xml>"""
    return s


@pytest.fixture(scope="module")
def Dict(request):
    message = {
            'ToUserName': 'rec',
            'FromUserName': 'sender',
            'CreateTime':1232322,
            'Content':'how are you',
            'MsgType':'text',
            }
    return message
