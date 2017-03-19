#!/usr/bin/env python
# -*- coding: utf8 -*-

from app.xaninos.mikrotik import handler

def get_test():
    assert(handler._tag() is not handler._tag())
