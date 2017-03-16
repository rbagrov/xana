#!/usr/bin/env python
# -*- coding: utf8 -*-

from app.protocols import telnet

def telnet_parameters_test():
    tn = telnet(host = '127.0.0.1', port = 23, login_string='Login: ', password_string='Password: ', prompt='> ', username='user', password='password')
    assert(tn.host and tn.port and tn.login_string and tn.password_string and tn.prompt and tn.username and tn.password)
