#!/usr/bin/env python
# -*- coding: utf8 -*-

from app.config.devices import Structure

def extract_xml_files_test():
    assert type(Structure.get_xml_files('examples')) is Structure.get_xml_files.__annotations__['return']
