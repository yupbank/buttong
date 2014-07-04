#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
framework.py
Author: yupbank
Email:  yupbank@gmail.com

Created on
2014-07-03
'''
from urllib import urlencode


class BaseTestCase(object):
    pass


class HTTPClientMixin(BaseTestCase):
   def get(self, url, data=None, headers=None):
       if data is not None:
           if isinstance(data, dict):
               data = urlencode(data)
           if '?' in url:
               url += '&amp;%s' % data
           else:
               url += '?%s' % data
       return self._fetch(url, 'GET', headers=headers)

   def post(self, url, data, headers=None, **kwargs):
       if data is not None:
           if isinstance(data, dict):
               data = urlencode(data)
       return self._fetch(url, 'POST', data, headers, **kwargs)

   def _fetch(self, url, method, data=None, headers=None, **kwargs):
       self.http_client.fetch(self.get_url(url), self.stop, method=method,
                              body=data, headers=headers, **kwargs)
       return self.wait()
