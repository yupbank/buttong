#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
ctrl.py
Author: yupbank
Email:  yupbank@gmail.com

Created on
2014-07-03
'''
from functools import partial

from settings import help_message, welcome_message
from util import form_message, toDict
from search import suggestion

def is_event(message_type):
    return message_type == 'event'

def is_text_message(message_type):
    return message_type == 'text'

def get_messeage_type(xdict):
    return xdict.get('MsgType') 

def get_event_type(xdict):
    return xdict.get('Event')

def is_subscibe(event_type):
    return event_type == 'subscribe'

def is_unsubscibe(event_type):
    return event_type == 'unsubscribe'

def get_text(xdict):
    return xdict.get('Content')

def is_help(text):
    return text.strip().lower() == 'help'

def is_query(text):
    return text.strip().lower().startswith('q:')

def subscribe(xdict):
    message = welcome_message+'\n'+help_message 
    return message

def router(xdict, callback):
    return_message = None
    message_type = get_messeage_type(xdict)
    if is_event(message_type):
        event_type = get_event_type(xdict)
        if is_subscibe(event_type):
            return_message = subscribe(xdict)
        elif is_unsubscibe(event_type):
            return unsubscribe(xdict)
    elif is_text_message(message_type):
        text = get_text(xdict)
        if is_help(text):
            return_message = help_message
        elif is_query(text):
            query(text, xdict, callback)
            return None
        else:
            return_message = text
    return return_message

def query(text, xdict, callback):
    query_text = text.strip('q:')
    suggestion(query_text, partial(callback, xdict))


def unsubscribe(xdict):
    return None

def return_back(xdict, callback):
    return_message = router(xdict, callback)
    if return_message:
        return form_message(xdict, return_message)

