#!/usr/bin/env python
# -*- coding: utf8 -*-

from app.protocols import ssh

def ssh_parameters_test():
    ss = ssh(host = '127.0.0.1', port = 22, username='user', password='password')
    assert(ss.host and ss.port, ss.username and ss.password)
