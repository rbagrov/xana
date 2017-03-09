#!/usr/bin/env python
# -*- coding: utf8 -*-

from app.config.devices import Parser

def read_yaml_test():
    path = 'examples/grouped-devices/groupA/GroupA1/group2.yaml'
    assert type(Parser.read_yaml(path)) is Parser.read_yaml.__annotations__['return']
