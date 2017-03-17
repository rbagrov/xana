#!/usr/bin/env python
# -*- coding: utf8 -*-

from app import data_type_validator


class ssh(object):

    def __init__(self, host, port, username, password):
        """
        Basic ssh object constructor
        """
        import paramiko
        ssh_params = ssh._add_ssh_parameters(host, port, username, password)
        self.host = ssh_params[0]
        self.port = ssh_params[1]
        self.username = ssh_params[2]
        self.password = ssh_params[3]

    @data_type_validator
    def _add_ssh_parameters(host: str, port: int, username: str, password: str):
        return (host, port, username, password)


class telnet(object):

    def __init__(self, host, port, login_string, password_string, prompt, username, password):
        """
        Basic telnet object constructor
        """
        from telnetlib import Telnet
        code_table = 'ascii'
        telnet_params = telnet._add_telnet_parameters(host, port, login_string, password_string, prompt, username, password)
        self.host = telnet_params[0]
        self.port = telnet_params[1]
        self.login_string = telnet_params[2].encode(code_table)
        self.password_string = telnet_params[3].encode(code_table)
        self.prompt = telnet_params[4].encode(code_table)
        self.username = telnet_params[5].encode(code_table)
        self.password = telnet_params[6].encode(code_table)
        self.telnet_obj = Telnet()

    @data_type_validator
    def _add_telnet_parameters(host: str, port: int, login_string: str, password_string: str, prompt: str, username: str, password: str):
        return (host, port, login_string, password_string, prompt, username, password)

    def _do_login(self):
        """
        Passes login checkpoint
        """
        self.telnet_obj.read_until(self.login_string)
        self.telnet_obj.write(self.username + b'\n')

    def _do_password(self):
        """
        Passes password checkpoint
        """
        self.telnet_obj.read_until(self.password_string)
        self.telnet_obj.write(self.password + b'\n')
        self.telnet_obj.read_until(self.prompt)

    def _do_open_connection(self):
        """
        Opens new socket for telnet
        """
        self.telnet_obj.open(self.host, self.port)

    def _do_close_connection(self):
        """
        Closes open instance socket for telnet
        """
        self.telnet_obj.close()

    def _connect(self):
        """
        Connects to target ip using custom login and password strings
        """
        self._do_open_connection()
        self._do_login()
        self._do_password()

    def instruct(self, command):
        """
        Send instruction to destination device
        """
        # Create empty response object
        response = []

        # Connect to destination device
        self._connect()

        # Apply instruction
        self.telnet_obj.write(command.encode('ascii') + b'\r\n')

        # Read response
        response.append(self.telnet_obj.read_until(self.prompt).replace(b'\r', b' '))

        self._do_close_connection()

        if response:
            return response
        else:
            return None
