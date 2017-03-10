#!/usr/bin/env python
# -*- coding: utf8 -*-

from app.config.devices import Parser

def read_xml_test():
    path = 'examples/grouped-devices/groupB/group4.xml'
    assert type(Parser.read_xml(path)) is Parser.read_xml.__annotations__['return']
