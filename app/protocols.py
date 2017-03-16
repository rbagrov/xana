#!/usr/bin/env python
# -*- coding: utf8 -*-


class telnet(object):

    def __init__(self, host, port, login_string, password_string, prompt, username, password):
        """
        Basic telnet object constructor
        """
        from telnetlib import Telnet
        code_table = 'ascii'
        self.host = host
        self.port = port
        self.login_string = login_string.encode(code_table)
        self.password_string = password_string.encode(code_table)
        self.prompt = prompt.encode(code_table)
        self.username = username.encode(code_table)
        self.password = password.encode(code_table)
        self.telnet_obj = Telnet()

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
