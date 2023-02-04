from packet.Packet import Packet
from utils.Packer import Packer

class NameTransferPacket(Packet):
    def __init__(self, name):
        super(NameTransferPacket, self).__init__(0, name)

    def serilize(self) -> bytes:
        buffer = bytes()

        buffer = Packer.writeUnsingedShort(buffer, self.id)
        buffer = Packer.writeString(buffer, self.data.encode())

        return buffer