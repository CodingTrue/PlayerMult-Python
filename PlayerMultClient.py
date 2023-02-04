import socket
import logging
from sys import stdout

from playermulttypes.SendType import SendType
from network.Connection import Connection

class PlayerMultClient:
    def __init__(self, hostIP: str, hostPort: int):
        self.hostIP = hostIP
        self.hostPort = hostPort

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)