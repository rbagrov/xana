#!/usr/bin/env python
# -*- coding: utf8 -*-

import logging
import logging.handlers


class Debug:
    enabled= False

if Debug.enabled:
    log = logging.getLogger(__name__)
    log.setLevel(logging.INFO)
else:
    log = logging.getLogger(__name__)
    log.setLevel(logging.ERROR)

syslog_handler = logging.handlers.SysLogHandler(address='/dev/log')

formatter = logging.Formatter('%(module)s.%(funcName)s: %(message)s')

syslog_handler.setFormatter(formatter)

log.addHandler(syslog_handler)
