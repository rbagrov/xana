#!/usr/bin/env python
# -*- coding: utf8 -*-

from app.config.devices import Structure

def extract_file_list_test():
    assert type(Structure.get_file_list('examples')) is Structure.get_file_list.__annotations__['return']
