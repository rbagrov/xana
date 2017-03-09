#!/usr/bin/env python
# -*- coding: utf8 -*-

import os

__title__ = 'Structure runner'
__all__ = ['Structure']
__author__ = 'Rostislav Bagrov <bagrov.rostislav@gmail.com>'


class Structure(object):

    def get_directory_structure(self, confdir: str) -> dict:
        """
        Creates a nested dictionary representing folder structure of confdir
        """
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

    def get_file_list(self, confdir: str) -> list:
        """
        Creates list of all files in the given directory structure
        """
        paths = []
        for root, dirs, files in os.walk(confdir):
            for filename in files:
                filepath = os.path.join(root, filename)
                paths.append(filepath)
        return paths

    def get_ini_files(self, confdir: str) -> list:
        """
        Creates list of all files with .ini extension in the given
        directory structure
        """
        return [f for f in self.get_file_list(confdir) if f.endswith('.ini')]

    def get_xml_files(self, confdir: str) -> list:
        """
        Creates list of all files with .xml extension in the given
        directory structure
        """
        return [f for f in self.get_file_list(confdir) if f.endswith('.xml')]

    def get_yaml_files(self, confdir: str) -> list:
        """
        Creates list of all files with .yaml extension in the given
        directory structure
        """
        return [f for f in self.get_file_list(confdir) if f.endswith('.yaml')]

    def get_json_files(self, confdir: str) -> list:
        """
        Creates list of all files with .yml extension in the given
        directory structure
        """
        return [f for f in self.get_file_list(confdir) if f.endswith('.json')]
