#!/usr/bin/env python
# -*- coding: utf8 -*-

from app.config.devices import Structure

def extract_file_list_test():
    dev = Structure()
    assert type(dev.get_file_list('examples')) is dev.get_file_list.__annotations__['return']
