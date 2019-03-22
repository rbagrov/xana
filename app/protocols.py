#!/usr/bin/env python
# -*- coding: utf8 -*-

from app import data_type_validator
from Log import log


class ssh(object):

    def __init__(self, hostname, port, username, password):
        """
        Basic ssh object constructor
        """
        import paramiko
        ssh_params = ssh._add_ssh_parameters(hostname, port, username, password)
        self.hostname = ssh_params[0]
        self.port = ssh_params[1]
        self.username = ssh_params[2]
        self.password = ssh_params[3]
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    @data_type_validator
    def _add_ssh_parameters(hostname: str, port: int, username: str, password: str):
        """
        Instance data type loop
        """
        return (hostname, port, username, password)

    def _connect(self):
        """
        Establishes ssh connection with given session parameters
        """
        try:
            self.ssh.connect(hostname=self.hostname,
                             port=self.port,
                             username=self.username,
                             password=self.password,
                             allow_agent=False,
                             look_for_keys=False)
        except Exception as e:
            log.error(e)

    def _disconnect(self):
        """
        Closes session
        """
        try:
            self.ssh.close()
        except Exception as e:
            log.error(e)

    def instruct(self, command: str):
        """
        Sends instruction to a device
        """
        self._connect()
        try:
            stdin, stdout, stderr = self.ssh.exec_command(command)
            out = stdout.read()
            self._disconnect()
            return out
        except Exception as e:
            log.error(e)

    def sftp(self):
        """
        Opens sftp client connection
        """
        self._connect()
        return self.ssh.open_sftp()


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
