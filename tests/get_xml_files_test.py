#!/usr/bin/env python
# -*- coding: utf8 -*-

from app.config.devices import Structure

def extract_xml_files_test():
    dev = Structure()
    assert type(dev.get_xml_files('examples')) is dev.get_xml_files.__annotations__['return']
