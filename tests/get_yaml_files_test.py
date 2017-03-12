#!/usr/bin/env python
# -*- coding: utf8 -*-

from app.config.devices import Structure

def extract_yaml_files_test():
    assert type(Structure.get_yaml_files('examples')) is Structure.get_yaml_files.__annotations__['return']
