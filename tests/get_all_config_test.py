#!/usr/bin/env python
# -*- coding: utf8 -*-

from app.config.devices import Parser

def get_all_config_test():
    path = 'examples'
    assert type(Parser.get_all_config(path)) is Parser.get_all_config.__annotations__['return']
