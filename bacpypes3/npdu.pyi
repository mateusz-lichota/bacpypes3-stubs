"""
This type stub file was generated by pyright.
"""

from typing import Callable, List, Optional, Tuple
from .debugging import DebugContents, bacpypes_debugging
from .comm import Client, Server
from .pdu import Address, PCI, PDU, PDUData

"""
Network Layer Protocol Data Units
"""
_debug = ...
_log = ...
npdu_types = ...
def register_npdu_type(class_):
    ...

@bacpypes_debugging
class NPCI(PCI, DebugContents):
    _debug: Callable[..., None]
    _debug_contents: Tuple[str, ...] = ...
    whoIsRouterToNetwork = ...
    iAmRouterToNetwork = ...
    iCouldBeRouterToNetwork = ...
    rejectMessageToNetwork = ...
    routerBusyToNetwork = ...
    routerAvailableToNetwork = ...
    initializeRoutingTable = ...
    initializeRoutingTableAck = ...
    establishConnectionToNetwork = ...
    disconnectConnectionToNetwork = ...
    challengeRequest = ...
    securityPayload = ...
    securityResponse = ...
    requestKeyUpdate = ...
    updateKeySet = ...
    updateDistributionKey = ...
    requestMasterKey = ...
    setMasterKey = ...
    whatIsNetworkNumber = ...
    networkNumberIs = ...
    npduVersion: int = ...
    npduControl = ...
    npduDADR: Optional[Address] = ...
    npduSADR: Optional[Address] = ...
    npduHopCount: int
    npduNetMessage: Optional[int] = ...
    npduVendorID: int
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    def update(self, npci): # -> None:
        ...
    
    def encode(self) -> PDU:
        """Encode the contents of the NPCI as a PDU."""
        ...
    
    @classmethod
    def decode(class_, pdu: PDU) -> NPCI:
        """decode the contents of the PDU and return an NPCI."""
        ...
    
    def npci_contents(self, use_dict=..., as_class=...): # -> dict[Any, Any]:
        """Return the contents of an object as a dict."""
        ...
    


@bacpypes_debugging
class NPDU(NPCI, PDUData):
    """
    Network Layer Protocol Data Unit
    """
    _debug: Callable[..., None]
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    def encode(self) -> PDU:
        ...
    
    @classmethod
    def decode(class_, pdu: PDU) -> NPDU:
        ...
    
    def npdu_contents(self, use_dict=..., as_class=...): # -> Dict[str, Any]:
        ...
    
    def dict_contents(self, use_dict=..., as_class=...): # -> Dict[str, Any]:
        """Return the contents of an object as a dict."""
        ...
    


@bacpypes_debugging
class NetworkCodec(Client[PDU], Server[NPDU]):
    _debug: Callable[..., None]
    def __init__(self, cid=..., sid=...) -> None:
        ...
    
    async def indication(self, npdu: NPDU) -> None:
        ...
    
    async def confirmation(self, pdu: PDU) -> None:
        ...
    


@bacpypes_debugging
def key_value_contents(use_dict=..., as_class=..., key_values=...): # -> dict[Any, Any]:
    """Return the contents of an object as a dict."""
    ...

@register_npdu_type
class WhoIsRouterToNetwork(NPDU):
    _debug_contents: Tuple[str, ...] = ...
    pduType = ...
    wirtnNetwork: Optional[int]
    def __init__(self, net: Optional[int] = ..., *args, **kwargs) -> None:
        ...
    
    def encode(self) -> PDU:
        ...
    
    @classmethod
    def decode(class_, pdu: PDU) -> NPDU:
        ...
    
    def npdu_contents(self, use_dict=..., as_class=...): # -> dict[Any, Any]:
        ...
    


@register_npdu_type
class IAmRouterToNetwork(NPDU):
    _debug_contents: Tuple[str, ...] = ...
    pduType = ...
    iartnNetworkList: List[int]
    def __init__(self, network_list: List[int] = ..., *args, **kwargs) -> None:
        ...
    
    def encode(self) -> PDU:
        ...
    
    @classmethod
    def decode(class_, pdu: PDU) -> NPDU:
        ...
    
    def npdu_contents(self, use_dict=..., as_class=...): # -> dict[Any, Any]:
        ...
    


@register_npdu_type
class ICouldBeRouterToNetwork(NPDU):
    _debug_contents: Tuple[str, ...] = ...
    pduType = ...
    icbrtnNetwork: int
    icbrtnPerformanceIndex: int
    def __init__(self, network: int, performance_index: int, *args, **kwargs) -> None:
        ...
    
    def encode(self) -> PDU:
        ...
    
    @classmethod
    def decode(class_, pdu: PDU) -> NPDU:
        ...
    
    def npdu_contents(self, use_dict=..., as_class=...): # -> dict[Any, Any]:
        ...
    


@register_npdu_type
class RejectMessageToNetwork(NPDU):
    _debug_contents: Tuple[str, ...] = ...
    pduType = ...
    rmtnRejectionReason: int
    rmtnDNET: int
    def __init__(self, reason: int, dnet: int, *args, **kwargs) -> None:
        ...
    
    def encode(self) -> PDU:
        ...
    
    @classmethod
    def decode(class_, pdu: PDU) -> NPDU:
        ...
    
    def npdu_contents(self, use_dict=..., as_class=...): # -> dict[Any, Any]:
        ...
    


@register_npdu_type
class RouterBusyToNetwork(NPDU):
    _debug_contents: Tuple[str, ...] = ...
    pduType = ...
    rbtnNetworkList: List[int]
    def __init__(self, network_list: List[int], *args, **kwargs) -> None:
        ...
    
    def encode(self) -> PDU:
        ...
    
    @classmethod
    def decode(class_, pdu: PDU) -> NPDU:
        ...
    
    def npdu_contents(self, use_dict=..., as_class=...): # -> dict[Any, Any]:
        ...
    


@register_npdu_type
class RouterAvailableToNetwork(NPDU):
    _debug_contents: Tuple[str, ...] = ...
    pduType = ...
    ratnNetworkList: List[int]
    def __init__(self, network_list: List[int], *args, **kwargs) -> None:
        ...
    
    def encode(self) -> PDU:
        ...
    
    @classmethod
    def decode(class_, pdu: PDU) -> NPDU:
        ...
    
    def npdu_contents(self, use_dict=..., as_class=...): # -> dict[Any, Any]:
        ...
    


class RoutingTableEntry(DebugContents):
    _debug_contents: Tuple[str, ...] = ...
    rtDNET: int
    rtPortID: int
    rtPortInfo: bytes
    def __init__(self, dnet: int, port_id: int, port_info: bytes) -> None:
        ...
    
    def __eq__(self, other) -> bool:
        """Return true iff entries are identical."""
        ...
    
    def dict_contents(self, use_dict=..., as_class=...): # -> dict[Any, Any]:
        """Return the contents of an object as a dict."""
        ...
    


@register_npdu_type
class InitializeRoutingTable(NPDU):
    pduType = ...
    _debug_contents: Tuple[str, ...] = ...
    irtTable: List[RoutingTableEntry]
    def __init__(self, routing_table: List[RoutingTableEntry], *args, **kwargs) -> None:
        ...
    
    def encode(self) -> PDU:
        ...
    
    @classmethod
    def decode(class_, pdu: PDU) -> NPDU:
        ...
    
    def npdu_contents(self, use_dict=..., as_class=...): # -> dict[Any, Any]:
        ...
    


@register_npdu_type
class InitializeRoutingTableAck(NPDU):
    pduType = ...
    _debug_contents: Tuple[str, ...] = ...
    irtaTable: List[RoutingTableEntry]
    def __init__(self, routing_table: List[RoutingTableEntry], *args, **kwargs) -> None:
        ...
    
    def encode(self) -> PDU:
        ...
    
    @classmethod
    def decode(class_, pdu: PDU) -> NPDU:
        ...
    
    def npdu_contents(self, use_dict=..., as_class=...): # -> dict[Any, Any]:
        ...
    


@register_npdu_type
class EstablishConnectionToNetwork(NPDU):
    _debug_contents: Tuple[str, ...] = ...
    pduType = ...
    ectnDNET: int
    ectnTerminationTime: int
    def __init__(self, dnet: int, termination_time: int, *args, **kwargs) -> None:
        ...
    
    def encode(self) -> PDU:
        ...
    
    @classmethod
    def decode(class_, pdu: PDU) -> NPDU:
        ...
    
    def npdu_contents(self, use_dict=..., as_class=...): # -> dict[Any, Any]:
        ...
    


@register_npdu_type
class DisconnectConnectionToNetwork(NPDU):
    _debug_contents: Tuple[str, ...] = ...
    pduType = ...
    dctnDNET: int
    def __init__(self, dnet: int, *args, **kwargs) -> None:
        ...
    
    def encode(self) -> PDU:
        ...
    
    @classmethod
    def decode(class_, pdu: PDU) -> NPDU:
        ...
    
    def npdu_contents(self, use_dict=..., as_class=...): # -> dict[Any, Any]:
        ...
    


@register_npdu_type
class WhatIsNetworkNumber(NPDU):
    _debug_contents: Tuple[str, ...] = ...
    pduType = ...
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    def encode(self) -> PDU:
        ...
    
    @classmethod
    def decode(class_, pdu: PDU) -> NPDU:
        ...
    
    def npdu_contents(self, use_dict=..., as_class=...): # -> dict[Any, Any]:
        ...
    


@register_npdu_type
class NetworkNumberIs(NPDU):
    _debug_contents: Tuple[str, ...] = ...
    pduType = ...
    nniNet: int
    nniFlag: int
    def __init__(self, net: int, flag: int, *args, **kwargs) -> None:
        ...
    
    def encode(self) -> PDU:
        ...
    
    @classmethod
    def decode(class_, pdu: PDU) -> NPDU:
        ...
    
    def npdu_contents(self, use_dict=..., as_class=...): # -> dict[Any, Any]:
        ...
    


