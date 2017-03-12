#!/usr/bin/env python
# -*- coding: utf8 -*-

from app.config.devices import Structure

def structure_walk_test():
    assert type(Structure.get_directory_structure('examples')) is Structure.get_directory_structure.__annotations__['return']
