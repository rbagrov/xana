#!/usr/bin/env python
# -*- coding: utf8 -*-

from app.config.devices import Structure

def extract_ini_files_test():
    assert type(Structure.get_ini_files('examples')) is Structure.get_ini_files.__annotations__['return']
