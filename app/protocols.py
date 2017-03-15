#!/usr/bin/env python
# -*- coding: utf8 -*-

import telnetlib
from collections import namedtuple

telnet_parameters = namedtuple('telnet_parameters', 'host port login password')
