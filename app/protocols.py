#!/usr/bin/env python
# -*- coding: utf8 -*-

import telnetlib


class telnet(object):

    def __init__(self, host: str, port: int, login: str, password: str):
        self.host = host
        self.port = port
        self.login = login
        self.password = password
        self.t = telnetlib.Telnet(host, port)
