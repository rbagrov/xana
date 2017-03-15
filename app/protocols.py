#!/usr/bin/env python
# -*- coding: utf8 -*-

import telnetlib
from collections import namedtuple

telnet_parameters = namedtuple('telnet_parameters', 'host port login password')

class telnet(object):

    def __init__(self, host):
        self.t_obj = telnetlib.Telnet(host)

    def connect(self):
        pass
