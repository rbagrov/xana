#!/usr/bin/env python
# -*- coding: utf8 -*-

from app.protocols import ssh

def ssh_parameters_test():
    ss = ssh(hostname = '127.0.0.1', port = 22, username='user', password='password')
    assert(ss.hostname and ss.port, ss.username and ss.password)
