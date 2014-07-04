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

@pytest.fixture(scope="function", params=[['text', 'how'], ['event', 'subscribe'], ['event', 'unsubscribe'],['text', u'q:中环']])
def xml(request):
    s = """<xml>
    <ToUserName><![CDATA[rec]]></ToUserName>
    <FromUserName><![CDATA[sender]]></FromUserName>
    <CreateTime>1232322</CreateTime>
    <MsgType><![CDATA[%s]]></MsgType>
    <%s><![CDATA[%s]]></%s>
    </xml>"""
    _type, mes = request.param
    if _type == 'event':
        return s%('event', 'Event', mes, 'Event')
    elif _type == 'text':
        return s%('text', 'Content', mes, 'Content')



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
    
