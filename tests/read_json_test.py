#!/usr/bin/env python
# -*- coding: utf8 -*-

from app.config.devices import Parser

def read_json_test():
    path = 'examples/grouped-devices/groupB/group3.json'
    assert type(Parser.read_json(path)) is Parser.read_json.__annotations__['return']
