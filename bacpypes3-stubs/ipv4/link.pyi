"""
This type stub file was generated by pyright.
"""

from ..debugging import bacpypes_debugging
from ..pdu import IPv4Address
from ..ipv4 import IPv4DatagramServer
from .bvll import BVLLCodec
from .service import BIPBBMD, BIPForeign, BIPNormal, UDPMultiplexer

"""
Link Layer Module

Classes in this module extend the BVLLServiceAccessPoint subclasses with
additional components necessary to send packets own to the physical network,
including a UDP multiplexer to distinguish between Annex-H and Annex-J traffic
anda IPv4DatagramServer instance to send and receive UDP packetes.

The clients of instances of these object (next up the stack) is a NetworkAdapter
instance which references a NetworkServiceAccessPoint.
"""
_debug = ...
_log = ...

class NormalLinkLayer(BIPNormal):
    """
    Create a link layer mini-stack starting with the "normal"
    BVLLServiceAccessPoint (parent class of BIPNormal) down to the datagram
    server.
    """

    codec: BVLLCodec
    multiplexer: UDPMultiplexer
    server: IPv4DatagramServer
    def __init__(self, local_address: IPv4Address, **kwargs) -> None: ...
    def close(self):  # -> None:
        ...

class ForeignLinkLayer(BIPForeign):
    """
    Create a link layer mini-stack starting with the "foreign"
    BVLLServiceAccessPoint (parent class of BIPForeign) down to the datagram
    server.
    """

    codec: BVLLCodec
    multiplexer: UDPMultiplexer
    server: IPv4DatagramServer
    def __init__(self, local_address: IPv4Address, **kwargs) -> None: ...
    def close(self):  # -> None:
        ...

class BBMDLinkLayer(BIPBBMD):
    """
    Create a link layer mini-stack starting with the BBMD
    BVLLServiceAccessPoint (parent class of BIPBBMD) down to the datagram
    server.
    """

    codec: BVLLCodec
    multiplexer: UDPMultiplexer
    server: IPv4DatagramServer
    def __init__(self, local_address: IPv4Address, **kwargs) -> None: ...
    def close(self):  # -> None:
        ...
