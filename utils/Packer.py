import struct

class Packer:
    @staticmethod
    def writeShort(buffer: bytes, data: int) -> bytes:
        buffer += struct.pack("h", data)
        return buffer

    @staticmethod
    def writeUnsingedShort(buffer: bytes, data: int) -> bytes:
        buffer += struct.pack("H", data)
        return buffer

    @staticmethod
    def writeInt(buffer: bytes, data: int) -> bytes:
        buffer += struct.pack("i", data)
        return buffer

    @staticmethod
    def writeUnsignedInt(buffer: bytes, data: int) -> bytes:
        buffer += struct.pack("I", data)
        return buffer

    @staticmethod
    def writeString(buffer: bytes, data: str):
        buffer += struct.pack(f"{len(data)}s", data)
        return buffer

    @staticmethod
    def readShort(data: bytes) -> bytes:
        return struct.unpack("h", data)[0]

    @staticmethod
    def readUnsingedShort(data: bytes) -> bytes:
        return struct.unpack("H", data)[0]

    @staticmethod
    def readInt(data: bytes) -> bytes:
        return struct.unpack("i", data)[0]

    @staticmethod
    def readUnsignedInt(data: bytes) -> bytes:
        return struct.unpack("I", data)[0]

    @staticmethod
    def readString(data: bytes):
        return struct.unpack(f"{len(data)}s", data)