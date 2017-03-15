#!/usr/bin/env python
# -*- coding: utf8 -*-

from app.protocols import telnet_parameters

def telnet_parameters_test():
    assert(telnet_parameters(1,2,3,4))
