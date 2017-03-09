#!/usr/bin/env python
# -*- coding: utf8 -*-

from app.config.devices import Parser

def read_ini_test():
    path = 'examples/grouped-devices/groupA/group5.ini'
    assert type(Parser.read_ini(path)) is Parser.read_ini.__annotations__['return']
