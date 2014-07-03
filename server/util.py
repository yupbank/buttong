#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
util.py
Author: yupbank
Email:  yupbank@gmail.com

Created on
2014-07-03
'''
import time
from hashlib import sha1
import string
from zh_wiki import zh2Hant, zh2Hans

ensure_tradition = lambda x: ''.join(map(lambda y: zh2Hant.get(y, y), x))

ensure_simple = lambda x: ''.join(map(lambda y: zh2Hans.get(y, y), x))


try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

from settings import TOKEN, XMLTEMPLATE

def valid(signature, timestamp, nonce):
    li = []

    li.append(TOKEN)
    li.append(nonce)
    li.append(timestamp)

    li.sort()

    tmpWord = ''.join(li)
    tmpWord = sha1(tmpWord).hexdigest()

    return tmpWord == signature
    
def toDict(xml):
    root = ET.fromstring(xml)
    return dict([ (x.tag, x.text) for x in root.findall('*') if x.tag != 'xml' ])
    
def toXml(kw):
    st = string.Template(XMLTEMPLATE)
    return st.substitute(kw)

def form_message(xdict, message):
    kw = dict.fromkeys(['ToUserName', 'FromUserName', 'CreateTime', 'Content'])
    kw['ToUserName'] = xdict['FromUserName']
    kw['FromUserName'] = xdict['ToUserName']
    kw['CreateTime'] = int(time.time())
    kw['Content'] = return_message
    return toXml(kw)

