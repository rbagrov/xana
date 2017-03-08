#!/usr/bin/env python
# -*- coding: utf8 -*-

from app.config.devices import Structure

def extract_yml_files_test():
    dev = Structure()
    assert type(dev.get_yml_files('examples')) is dev.get_yml_files.__annotations__['return']
