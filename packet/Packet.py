import logging

from utils.Packer import Packer

class Packet:
    packets = {}

    @classmethod
    def registerPacket(cls, id: int, packet):
        cls.packets[id] = packet
        logging.debug(f"Registered {packet.__name__}")

    @classmethod
    def isRegistered(cls, id: int) -> bool:
        return id in cls.packets

    @classmethod
    def getPacketByID(cls, id: int):
        if cls.isRegistered(id): return cls.packets.get(id)
        return None

    def __init__(self, id: int, data: any):
        self.id = id
        self.data = data

    def serilize(self) -> bytes:
        return bytes()