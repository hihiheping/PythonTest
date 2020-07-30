#! /usr/bin/env python3
# _*_ coding: utf-8 _*_

import paramiko
import time
import io

class sshClient():

    def __init__(self, ip, username, password, port=22):
        self.ip = ip
        self.username = username
        self.password = password
        self.port = port

    def connect(self, hostkeys_file=None):
        self._client = paramiko.SSHClient()
        self._client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            self._client.connect(self.ip, self.port, self.username, self.password, timeout=2, look_for_keys=False)
            self._channel = self._client.invoke_shell()
        except Exception as error:
            raise error
    
    #ssh命令发送函数
    def send(self, commands):
        response = []
        for command in commands:
            self._channel.send(command)
            time.sleep(0.3)
            response.append(self.receive())
        return response

    #命令回显函数
    def receive(self):
        #recv = io.StringIO()
        recv = io.BytesIO()
        while self._channel.recv_ready():
            data = self._channel.recv(10240)
            recv.write(data)
        return recv.getvalue()

    #回显命令保存到txt
    def write_to_txt(self, txt_name, content_list):
        #with open (txt_name, "w") as f:
        with open (txt_name, "wb+") as f:
            for content in content_list:
                f.write(content)

    #关闭ssh会话
    def close_ssh(self):
        self._client.close()

#ip_list = ['192.168.100.111', '192.168.100.112']
#ip_list = ['192.168.100.111']
ip_list = ['10.10.10.2']
command_list = [
    'more off\r\n',
    'show run\r\n',
    'show interface sw bri\r\n',
    'show ip interface bri\r\n',
    'show int loo0\r\n',
    'show ver\r\n',
    'conf ter\r\n',
    'int loo1\r\n',
    'ip add 11.11.11.11 32\r\n',
    'exit\r\n',
    'do show int loo1\r\n'
    ]

for ip in ip_list:
    ssh = sshClient(ip, 'admin', 'Pass.2020')
    ssh.connect()
    commands_response = ssh.send(command_list)
    txt_name = f"{ip}.txt"
    ssh.write_to_txt(txt_name, commands_response)
    ssh.close_ssh()
    print(f'{ip} collect ok')