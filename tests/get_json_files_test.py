#!/usr/bin/env python
# -*- coding: utf8 -*-

from app.config.devices import Structure

def extract_json_files_test():
    assert type(Structure.get_json_files('examples')) is Structure.get_json_files.__annotations__['return']
