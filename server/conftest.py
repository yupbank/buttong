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

from .util import valid
from .ctrl import router, is_event, is_text_message, is_subscibe, is_unsubscibe, is_help, is_query, get_messeage_type, get_event_type, get_text
from .app import application

@pytest.fixture(scope="module", params=['text', 'event'])
def xml(request):
    s = """<xml>
    <ToUserName><![CDATA[rec]]></ToUserName>
    <FromUserName><![CDATA[sender]]></FromUserName>
    <CreateTime>1232322</CreateTime>
    <MsgType><![CDATA[%s]]></MsgType>
    <Content><![CDATA[how are you]]></Content>
    </xml>"""%request.param
    return s



@pytest.fixture(scope="function", params=['text', 'event'])
def message(request):
    message = {
            'ToUserName': 'rec',
            'FromUserName': 'sender',
            'CreateTime':1232322,
            'Content':'how are you',
            'MsgType': request.param,
            }
    return message, request.param




    
