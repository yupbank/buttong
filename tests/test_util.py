#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
test_util.py
Author: yupbank
Email:  yupbank@gmail.com

Created on
2014-07-03
'''
from .framework import BaseTestCase
from ..conftest import valid, router, is_event, is_text_message, is_subscibe, is_unsubscibe, is_help, is_query, get_messeage_type, get_event_type, get_text, return_back, subscribe

class TestMessage(BaseTestCase):
    def test_valid(self, data_fortest):
        signature = data_fortest['signature']
        timestamp = data_fortest['timestamp']
        nonce = data_fortest['nonce']
        result = valid(signature, timestamp, nonce)
        assert result

    def test_messgae(self, message):
        def func(a):
            pass

        message_body, message_type = message
        _message_type = get_messeage_type(message_body)
        event_type, text = None, None
        assert message_type == _message_type
        if message_type == 'event':
            assert is_event(_message_type)
            event_type = get_event_type(message_body)

        if message_type == 'text':
            assert is_text_message(_message_type)
            text = get_text(message_body)

        return_message = router(message_body, func)
        if event_type:
            if is_subscibe(event_type):
                assert return_message == subscribe(message_body) 
            if is_unsubscibe(event_type):
                assert return_message is None

        if text:
            if is_help(text):
                assert return_message == help_message
            if is_query(text):
                assert return_message is None

    def test_return_back(self, message):
        message_body, message_type = message
        def callback(*args):
            return args
        if is_event(message_type):
            assert 'help' in return_back(message_body, callback)
        if is_text_message(message_type):
            assert 'text' in return_back(message_body, callback)
