#!/usr/bin/env python
# -*- coding: utf8 -*-

from app.config.devices import Structure

def structure_walk_test():
    dev = Structure()
    assert type(dev.get_directory_structure('examples')) is dev.get_directory_structure.__annotations__['return']
