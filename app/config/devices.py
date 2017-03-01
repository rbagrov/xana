#!/usr/bin/env python
# -*- coding: utf8 -*-

__title__ = 'Structure runner'
__all__ = ['Structure']
__author__ = 'Rostislav Bagrov <bagrov.rostislav@gmail.com>'

class Structure(object):

    def get_directory_structure(self, confdir: str) -> dict:
        """
        Creates a nested dictionary representing folder structure of confdir
        """
        import os
        from functools import reduce
        out = {}
        confdir = confdir.rstrip(os.sep)
        start = confdir.rfind(os.sep) + 1
        for path, dirs, files in os.walk(confdir):
            folders = path[start:].split(os.sep)
            subdir = dict.fromkeys(files)
            parent = reduce(dict.get, folders[:-1], out)
            parent[folders[-1]] = subdir
        return out
