import socket
import logging
from sys import stdout

from playermulttypes.SendType import SendType
from network.Connection import Connection

class PlayerMultServer:
    instance = None

    def __init__(self, ip: str, port: int, maxConnectionCount: int = 10, sendType: SendType = SendType.safe):
        PlayerMultServer.instance = self

        logging.basicConfig(format="[%(asctime)s] (%(levelname)s) %(message)s", level=logging.DEBUG, handlers=[
            logging.StreamHandler(stdout),
            logging.FileHandler("log.log", mode="w")
        ])

        self.ip = ip
        self.port = port

        self.maxConnectionCount = maxConnectionCount

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.ip, self.port))
        self.socket.settimeout(0.5)

        self.connections = []

    def addConnection(self, connection: Connection):
        self.connections.append(connection)

    def listen(self):
        try:
            s, address = self.socket.accept()

            logging.info(f"{address[0]} connected to Server")
            self.addConnection(Connection(s, address, "connection"))
        except socket.timeout: pass

    def tick(self):
        self.listen()

        for connection in self.connections:
            data = connection.socket.recv(2048)

            if not data: continue
            else: logging.info(data.decode("utf-8"))


    def start(self):
        logging.info("Starting Server...")
        self.socket.listen(self.maxConnectionCount)
        logging.info("Listening for connections...")

    def close(self):
        logging.info("Closing Server...")
        self.socket.close()