#!/usr/bin/env python
# -*- coding: utf8 -*-

from app.protocols import ssh
from app.protocols import telnet


def get_config(hostname, port, username, password, localpath):
    """
    Downloads config from RouterOS
    """
    session = ssh(hostname, port, username, password)
    rscfile = '{}.rsc'.format(_tag())
    session.instruct('/export file={}'.format(rscfile))
    sftp = session.sftp()
    localpath = '{}{}'.format(localpath, rscfile)
    try:
        sftp.get(rscfile, localpath, callback=_check_transfer)
    except (PermissionError,):
        pass
    session.instruct('/file remove {}'.format(rscfile))


def _check_transfer(got, should):
    """
    Callback for sftp put/get function.
    """
    if got == should:
        pass
    else:
        pass


def _tag():
    """
    Return random string later used for filename
    """
    import string
    import random
    count = 0
    charset = string.ascii_uppercase + string.ascii_lowercase + string.digits
    return ''.join(random.choice(charset) for each in range(8))


def set_config(hostname, port, username, password, localpath, remotepath):
    """
    Uploads config to RouterOS
    """
    ssh = protocols.ssh(hostname, port, username, password)
    sftp = ssh.sftp()
    sftp.put(localpath, remotepath, callback=_check_transfer)


def save_config():
    pass
