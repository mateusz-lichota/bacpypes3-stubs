"""
This type stub file was generated by pyright.
"""

from typing import Callable
from ..debugging import bacpypes_debugging
from ..object import AnalogInputObject as _AnalogInputObject, AnalogOutputObject as _AnalogOutputObject, AnalogValueObject as _AnalogValueObject
from .object import Object as _Object
from .cov import COVIncrementCriteria
from .cmd import Commandable
from .event import OutOfRangeEventAlgorithm
from .fault import OutOfRangeFaultAlgorithm

"""
Analog Input, Output, and Value Object
"""
_debug = ...
_log = ...
_vendor_id = ...
@bacpypes_debugging
class AnalogInputObject(_Object, _AnalogInputObject):
    """
    A local analog input object.
    """
    _debug: Callable[..., None]
    _cov_criteria = COVIncrementCriteria
    _required = ...


@bacpypes_debugging
class AnalogInputObjectIR(AnalogInputObject):
    """
    A local analog input object with intrinsic event reporting.
    """
    _debug: Callable[..., None]
    _event_algorithm: OutOfRangeEventAlgorithm
    _required = ...
    _optional = ...
    def __init__(self, **kwargs) -> None:
        ...
    


@bacpypes_debugging
class AnalogInputObjectFD(AnalogInputObject):
    """
    A local analog input object with fault detection.
    """
    _debug: Callable[..., None]
    _fault_algorithm: OutOfRangeFaultAlgorithm
    _required = ...
    def __init__(self, **kwargs) -> None:
        ...
    


@bacpypes_debugging
class AnalogOutputObject(Commandable, _Object, _AnalogOutputObject):
    """
    A local analog output object.
    """
    _debug: Callable[..., None]
    _cov_criteria = COVIncrementCriteria
    _required = ...


@bacpypes_debugging
class AnalogOutputObjectIR(AnalogOutputObject):
    """
    A local analog output object with intrinsic reporting.
    """
    _debug: Callable[..., None]
    _event_algorithm: OutOfRangeEventAlgorithm
    _required = ...
    _optional = ...
    def __init__(self, **kwargs) -> None:
        ...
    


@bacpypes_debugging
class AnalogValueObject(_Object, _AnalogValueObject):
    """
    Vanilla Analog Value Object
    """
    _debug: Callable[..., None]
    _cov_criteria = COVIncrementCriteria
    _required = ...


@bacpypes_debugging
class AnalogValueObjectCmd(Commandable, AnalogValueObject):
    """
    Commandable Analog Value Object
    """
    _required = ...


@bacpypes_debugging
class AnalogValueObjectIR(AnalogValueObjectCmd):
    """
    Commandable Analog Value Object with Intrinsic Reporting
    """
    _debug: Callable[..., None]
    _event_algorithm: OutOfRangeEventAlgorithm
    _required = ...
    _optional = ...
    def __init__(self, **kwargs) -> None:
        ...
    


@bacpypes_debugging
class AnalogValueObjectFD(AnalogValueObject):
    """
    A local analog input object with fault detection.
    """
    _debug: Callable[..., None]
    _fault_algorithm: OutOfRangeFaultAlgorithm
    _required = ...
    def __init__(self, **kwargs) -> None:
        ...
    


