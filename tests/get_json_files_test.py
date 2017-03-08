#!/usr/bin/env python
# -*- coding: utf8 -*-

from app.config.devices import Structure

def extract_json_files_test():
    dev = Structure()
    assert type(dev.get_json_files('examples')) is dev.get_json_files.__annotations__['return']
