# -*- coding: utf-8 -*-

import string
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
    
def toDict(xml):
    root = ET.fromstring(xml)
    return dict([ (x.tag, x.text) for x in root.findall('*') if x.tag != 'xml' ])
    
def toXml(kw):
    st = string.Template(s)
    return st.substitute(kw)
