#!/usr/bin/env python
# -*- coding: utf8 -*-

import os
from functools import reduce
from Log import log

__title__ = 'Structure runner'
__all__ = ['Structure']
__author__ = 'Rostislav Bagrov <bagrov.rostislav@gmail.com>'


class Structure(object):

    @staticmethod
    def get_directory_structure(confdir: str) -> dict:
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

    @staticmethod
    def get_file_list(confdir: str) -> list:
        """
        Creates list of all files in the given directory structure
        """
        paths = []
        for root, dirs, files in os.walk(confdir):
            for filename in files:
                filepath = os.path.join(root, filename)
                paths.append(filepath)
        return paths

    @staticmethod
    def get_ini_files(confdir: str) -> list:
        """
        Creates list of all files with .ini extension in the given
        directory structure
        """
        return [f for f in Structure.get_file_list(confdir) if f.endswith('.ini')]

    @staticmethod
    def get_xml_files(confdir: str) -> list:
        """
        Creates list of all files with .xml extension in the given
        directory structure
        """
        return [f for f in Structure.get_file_list(confdir) if f.endswith('.xml')]

    @staticmethod
    def get_yaml_files(confdir: str) -> list:
        """
        Creates list of all files with .yaml extension in the given
        directory structure
        """
        return [f for f in Structure.get_file_list(confdir) if f.endswith('.yaml')]

    @staticmethod
    def get_json_files(confdir: str) -> list:
        """
        Creates list of all files with .yml extension in the given
        directory structure
        """
        return [f for f in Structure.get_file_list(confdir) if f.endswith('.json')]


class Parser(object):

    @staticmethod
    def get_all_config(confdir: str) -> list:
        """
        Walks over confdir and returns parsed configs
        """
        out = []
        for each in Structure.get_json_files(confdir):
            out.append(Parser.read_json(each))
        for each in Structure.get_ini_files(confdir):
            out.append(Parser.read_ini(each))
        for each in Structure.get_yaml_files(confdir):
            out.append(Parser.read_yaml(each))
        for each in Structure.get_xml_files(confdir):
            out.append(Parser.read_xml(each))
        return out

    @staticmethod
    def read_json(cfile: str) -> list:
        """
        Opens JSON conf file and returns its contents.
        """
        import json
        try:
            with open(cfile, 'r') as json_file:
                return json.load(json_file)
        except Exception as e:
            log.error(e)

    @staticmethod
    def read_yaml(cfile: str) -> list:
        """
        Opens YAML conf file and returns its contents.
        """
        import yaml
        try:
            with open(cfile, 'r') as yaml_file:
                conf = yaml.load(yaml_file)
                return [each for each in conf.items()]
        except Exception as e:
            log.error(e)

    @staticmethod
    def read_ini(cfile: str) -> list:
        """
        Opens INI conf file and returns its contents.
        """
        from configparser import ConfigParser
        config = ConfigParser()
        out = []
        try:
            config.read(cfile)
            sections = config.sections()
            for section in sections:
                items = config.items(section)
                out.append({section: {item[0]: item[1] for item in items}})
            return out
        except Exception as e:
            log.error(e)

    @staticmethod
    def read_xml(cfile: str) -> list:
        """
        Opens XML conf file and returns its contents.
        """
        import xml.etree.ElementTree as xmlparser
        out = []
        try:
            tree = xmlparser.parse(cfile)
            root = tree.getroot()
            for device in root.findall('device'):
                out.append(
                    {device.attrib['name']:
                        {'ip': device.find('ip').text,
                         'user': device.find('user').text,
                         'password': device.find('password').text}})
            return out
        except Exception as e:
            log.error(e)
