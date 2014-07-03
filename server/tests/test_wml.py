#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
test.py
Author: yupbank
Email:  yupbank@gmail.com

Created on
2014-07-03
'''
import pytest
from framework import BaseTestCase
from wxml import toDict, toXml

class TestWml(BaseTestCase):
    def test_todict(self, xml, Dict):
        a = toDict(xml)
        for i in a:
            assert i in Dict


        
