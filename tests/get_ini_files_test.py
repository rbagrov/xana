#!/usr/bin/env python
# -*- coding: utf8 -*-

from app.config.devices import Structure

def extract_ini_files_test():
    dev = Structure()
    assert type(dev.get_ini_files('examples')) is dev.get_ini_files.__annotations__['return']
