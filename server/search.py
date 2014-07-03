#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
seach.py
Author: yupbank
Email:  yupbank@gmail.com

Created on
2014-07-03
'''
from tornado import web
from tornado import httpclient
from settings import API_BASE, SUGGETION
from util import ensure_tradition
http_worker = httpclient.AsyncHTTPClient()

def suggestion(q, callback):
    q = ensure_tradition(q)
    url = SUGGETION%q
    return query_search(url, callback)

def query_search(url, callback, request_timeout=1, **kwargs):
    http_worker.fetch(API_BASE+url, callback, request_timeout=request_timeout, **kwargs)

if __name__ == '__main__':
    main()
