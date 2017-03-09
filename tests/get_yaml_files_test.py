#!/usr/bin/env python
# -*- coding: utf8 -*-

from app.config.devices import Structure

def extract_yaml_files_test():
    dev = Structure()
    assert type(dev.get_yaml_files('examples')) is dev.get_yaml_files.__annotations__['return']
