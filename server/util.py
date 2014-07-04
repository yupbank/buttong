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

newzh2hant, newzh2hans = {}, {}

for j, k in zh2Hant.iteritems():
    new_j = j.decode('u8')
    new_k = k.decode('u8')
    newzh2hant[new_j] = new_k

for j, k in zh2Hans.iteritems():
    new_j = j.decode('u8')
    new_k = j.decode('u8')
    newzh2hans[new_j] = new_k

def ensure_tradition(words):
    res = u''
    for word in words:
        res += newzh2hant.get(word, word)
    return res
        

ensure_simple = lambda x: u''.join(map(lambda y: newzh2hans.get(y, y), x))


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
    kw['Content'] = message
    return toXml(kw)

