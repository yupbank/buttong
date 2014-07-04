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

from server.util import valid
from server.ctrl import router, is_event, is_text_message, is_subscibe, is_unsubscibe, is_help, is_query, get_messeage_type, get_event_type, get_text, return_back, subscribe
from server.app import application

@pytest.fixture(scope="module", params=[['text', 'how'], ['text', 'q:wa'], ['event', 'subscribe'], ['event', 'unsubscribe']])
def xml(request):
    _type, mes = request.param
    msgtype = 'Event' if _type == 'event' else 'MsgType'
    s = """<xml>
    <ToUserName><![CDATA[rec]]></ToUserName>
    <FromUserName><![CDATA[sender]]></FromUserName>
    <CreateTime>1232322</CreateTime>
    <%s><![CDATA[%s]]></%s>
    <Content><![CDATA[%s]]></Content>
    </xml>"""%(msgtype, mes, msgtype, _type)
    return s



@pytest.fixture(scope="module", params=['text', 'event'])
def message(request):
    message = {
            'ToUserName': 'rec',
            'FromUserName': 'sender',
            'CreateTime':1232322,
            'Content':'how are you',
            'Event':'subscribe',
            'MsgType': request.param,
            }
    return message, request.param


@pytest.fixture(scope="function", params=['text', 'event', u'中文恩'])
def echo_str(request):
    return request.param

@pytest.fixture(scope="function")
def data_fortest():
    data={'signature':'85a4c16cac34f23e633381a520c1e2bea244a1ce',
                                                'timestamp': '1404216147',
                                                'nonce':'1225742971'}
    return data
    
