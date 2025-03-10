"""
This type stub file was generated by pyright.
"""

from uuid import UUID
from typing import Callable, List, Optional, Tuple
from ..debugging import DebugContents, bacpypes_debugging
from ..pdu import PCI, PDU, PDUData, VirtualAddress
from ..comm import Client, Server
from ..basetypes import ErrorClass, ErrorCode

"""
BACnet Secure Connect Virtual Link Layer Protocol Data Units
"""
_debug = ...
_log = ...
pdu_types = ...

def register_bvlpdu_type(class_): ...

class HeaderOption(PDUData, DebugContents):
    """
    Header Option
    """

    _debug: Callable[..., None]
    _debug_contents: Tuple[str, ...] = ...
    debug_contents = ...
    option_type: int = ...
    header_data_flag: bool = ...
    must_understand: bool = ...
    more_options: bool = ...
    header_marker: int = ...
    header_length: int = ...
    def __init__(
        self,
        *args,
        option_type: int = ...,
        header_data_flag: bool = ...,
        must_understand: bool = ...,
        more_options: bool = ...,
        **kwargs,
    ) -> None: ...
    def encode(self) -> PDU:
        """Encode the contents of the HeaderOption into a PDU."""
        ...

    @classmethod
    def decode(class_, pdu: PDU) -> HeaderOption:
        """
        Decode the contents of the PDU and return a HeaderOption or one
        of its subclasses.
        """
        ...

class SecurePathHeaderOption(HeaderOption):
    def __init__(self) -> None: ...

class ProprietaryHeaderOption(HeaderOption):
    _debug: Callable[..., None]
    _debug_contents: Tuple[str, ...] = ...
    vendor_identifier: int = ...
    proprietary_option_type: int = ...
    def __init__(
        self,
        *args,
        vendor_identifier: int = ...,
        proprietary_option_type: int = ...,
        **kwargs,
    ) -> None: ...

class LPCI(PCI, DebugContents):
    """
    Link Layer Protocol Control Information
    """

    _debug: Callable[..., None]
    _debug_contents: Tuple[str, ...] = ...
    result = ...
    encapsulatedNPDU = ...
    addressResolution = ...
    addressResolutionACK = ...
    advertisement = ...
    advertisementSolicitation = ...
    connectRequest = ...
    connectAccept = ...
    disconnectRequest = ...
    disconnectACK = ...
    heartbeatRequest = ...
    heartbeatACK = ...
    proprietaryMessage = ...
    bvlcFunction: int
    bvlcControlFlags: int
    bvlcMessageID: int
    bvlcOriginatingVirtualAddress: Optional[VirtualAddress] = ...
    bvlcDestinationVirtualAddress: Optional[VirtualAddress] = ...
    bvlcDestinationOptions: List[HeaderOption]
    bvlcDataOptions: List[HeaderOption]
    def __init__(self, *args, **kwargs) -> None: ...
    def update(self, bvlci: LPCI) -> None: ...
    def encode(self) -> PDU:
        """Encode the contents of the LPCI into a PDU."""
        ...

    @classmethod
    def decode(class_, pdu: PDU) -> LPCI:
        """Decode the contents of the PDU and return a LPCI."""
        ...

    def lpci_contents(self, use_dict=..., as_class=...):  # -> dict[Any, Any]:
        """Return the contents of an object as a dict."""
        ...

class LPDU(LPCI, PDUData):
    """
    Link Layer Protocol Data Unit
    """
    def __init__(self, *args, **kwargs) -> None: ...
    def encode(self) -> PDU: ...
    @classmethod
    def decode(class_, pdu: PDU) -> LPDU: ...
    def lpdu_contents(self, use_dict=..., as_class=...) -> dict: ...
    def dict_contents(self, use_dict=..., as_class=...) -> dict:
        """Return the contents of an object as a dict."""
        ...

    debug_contents = ...

class BVLLCodec(Client[PDU], Server[LPDU]):
    _debug: Callable[..., None]
    def __init__(self, cid=..., sid=...) -> None: ...
    async def indication(self, lpdu: LPDU) -> None: ...
    async def confirmation(self, pdu: PDU) -> None: ...

def key_value_contents(
    use_dict=..., as_class=..., key_values=...
):  # -> dict[Any, Any]:
    """
    Update the contents of a dictionary with the keys and values that
    are not None, and if the value as a dict_contents() function then
    call it for nested details.
    """
    ...
@register_bvlpdu_type
class Result(LPDU):
    _debug: Callable[..., None]
    _debug_contents: Tuple[str, ...] = ...
    bvlcFunction = ...
    result_function: int
    result_code: int
    error_header_marker: int
    error_class: ErrorClass
    error_code: ErrorCode
    error_details: str
    def __init__(
        self,
        result_function: int,
        result_code: int,
        error_header_marker: int = ...,
        error_class: Optional[ErrorClass] = ...,
        error_code: Optional[ErrorCode] = ...,
        error_details: str = ...,
        *args,
        **kwargs,
    ) -> None: ...
    def encode(self) -> PDU: ...
    @classmethod
    def decode(class_, pdu: PDU) -> LPDU: ...
    def lpdu_contents(self, use_dict=..., as_class=...):  # -> dict[Any, Any]:
        """Return the contents of an object as a dict."""
        ...

@register_bvlpdu_type
class EncapsulatedNPDU(LPDU):
    _debug: Callable[..., None]
    _debug_contents: Tuple[str, ...] = ...
    bvlcFunction = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def encode(self) -> PDU: ...
    @classmethod
    def decode(class_, pdu: PDU) -> LPDU: ...
    def lpdu_contents(self, use_dict=..., as_class=...):  # -> dict[Any, Any]:
        """Return the contents of an object as a dict."""
        ...

@register_bvlpdu_type
class AddressResolution(LPDU):
    bvlcFunction = ...
    @classmethod
    def decode(class_, pdu: PDU) -> LPDU: ...

@register_bvlpdu_type
class AddressResolutionACK(LPDU):
    _debug: Callable[..., None]
    _debug_contents: Tuple[str, ...] = ...
    bvlcFunction = ...
    websocket_uris: str
    def __init__(self, websocket_uris: str = ..., *args, **kwargs) -> None: ...
    def encode(self) -> PDU: ...
    @classmethod
    def decode(class_, pdu: PDU) -> LPDU: ...
    def lpdu_contents(self, use_dict=..., as_class=...):  # -> dict[Any, Any]:
        """Return the contents of an object as a dict."""
        ...

@register_bvlpdu_type
class Advertisement(LPDU):
    _debug: Callable[..., None]
    _debug_contents: Tuple[str, ...] = ...
    bvlcFunction = ...
    hub_connection_status: int
    accept_direct_connections: int
    maximum_bvlc_length: int
    maximum_npdu_length: int
    def __init__(
        self,
        hub_connection_status: int,
        accept_direct_connections: int,
        maximum_bvlc_length: int,
        maximum_npdu_length: int,
        *args,
        **kwargs,
    ) -> None: ...
    def encode(self) -> PDU: ...
    @classmethod
    def decode(class_, pdu: PDU) -> LPDU: ...
    def lpdu_contents(self, use_dict=..., as_class=...):  # -> dict[Any, Any]:
        """Return the contents of an object as a dict."""
        ...

@register_bvlpdu_type
class AdvertisementSolicitation(LPDU):
    bvlcFunction = ...
    @classmethod
    def decode(class_, pdu: PDU) -> LPDU: ...

@register_bvlpdu_type
class ConnectRequest(LPDU):
    _debug: Callable[..., None]
    _debug_contents: Tuple[str, ...] = ...
    bvlcFunction = ...
    vmac_address: VirtualAddress
    device_uuid: UUID
    maximum_bvlc_length: int
    maximum_npdu_length: int
    def __init__(
        self,
        vmac_address: VirtualAddress,
        device_uuid: UUID,
        maximum_bvlc_length: int,
        maximum_npdu_length: int,
        *args,
        **kwargs,
    ) -> None: ...
    def encode(self) -> PDU: ...
    @classmethod
    def decode(class_, pdu: PDU) -> LPDU: ...
    def lpdu_contents(self, use_dict=..., as_class=...):  # -> dict[Any, Any]:
        """Return the contents of an object as a dict."""
        ...

@register_bvlpdu_type
class ConnectAccept(LPDU):
    _debug: Callable[..., None]
    _debug_contents: Tuple[str, ...] = ...
    bvlcFunction = ...
    vmac_address: VirtualAddress
    device_uuid: UUID
    maximum_bvlc_length: int
    maximum_npdu_length: int
    def __init__(
        self,
        vmac_address: VirtualAddress,
        device_uuid: UUID,
        maximum_bvlc_length: int,
        maximum_npdu_length: int,
        *args,
        **kwargs,
    ) -> None: ...
    def encode(self) -> PDU: ...
    @classmethod
    def decode(class_, pdu: PDU) -> LPDU: ...
    def lpdu_contents(self, use_dict=..., as_class=...):  # -> dict[Any, Any]:
        """Return the contents of an object as a dict."""
        ...

@register_bvlpdu_type
class DisconnectRequest(LPDU):
    bvlcFunction = ...
    @classmethod
    def decode(class_, pdu: PDU) -> LPDU: ...

@register_bvlpdu_type
class DisconnectACK(LPDU):
    bvlcFunction = ...
    @classmethod
    def decode(class_, pdu: PDU) -> LPDU: ...

@register_bvlpdu_type
class HeartbeatRequest(LPDU):
    bvlcFunction = ...
    @classmethod
    def decode(class_, pdu: PDU) -> LPDU: ...

@register_bvlpdu_type
class HeartbeatACK(LPDU):
    bvlcFunction = ...
    @classmethod
    def decode(class_, pdu: PDU) -> LPDU: ...

@register_bvlpdu_type
class ProprietaryMessage(LPDU):
    _debug: Callable[..., None]
    _debug_contents: Tuple[str, ...] = ...
    bvlcFunction = ...
    vendor_identifier: int
    proprietary_function: int
    def __init__(
        self, vendor_identifier: int, proprietary_function: int, *args, **kwargs
    ) -> None: ...
    def encode(self) -> PDU: ...
    @classmethod
    def decode(class_, pdu: PDU) -> LPDU: ...
    def lpdu_contents(self, use_dict=..., as_class=...):  # -> dict[Any, Any]:
        """Return the contents of an object as a dict."""
        ...
