from enum import Enum
from socket import SOCK_STREAM, SOCK_DGRAM

class SendType(Enum):
    safe = SOCK_STREAM
    fast = SOCK_DGRAM