"""
This type stub file was generated by pyright.
"""

from typing import Callable, Dict, Optional, Tuple
from .debugging import DebugContents, bacpypes_debugging

"""
Vendor
"""
_debug = ...
_log = ...
ASHRAE_vendor_info: VendorInfo
_vendor_info: Dict[int, VendorInfo] = ...

def get_vendor_info(vendor_identifier: int) -> VendorInfo: ...

class VendorInfo(DebugContents):
    _debug: Callable[..., None]
    _debug_contents: Tuple[str, ...] = ...
    vendor_identifier: int
    registered_object_classes: Dict[int, type] = ...
    object_type: type
    object_identifier: type
    property_identifier: type
    def __init__(
        self,
        vendor_identifier: int,
        object_type: Optional[type] = ...,
        property_identifier: Optional[type] = ...,
    ) -> None: ...
    def register_object_class(self, object_type: int, object_class: type) -> None: ...
    def get_object_class(self, object_type: int) -> Optional[type]: ...

ASHRAE_vendor_info = ...
