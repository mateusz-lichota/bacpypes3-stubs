"""
This type stub file was generated by pyright.
"""

import asyncio
from typing import Callable, List
from ..debugging import bacpypes_debugging

"""
Change Of Value
"""
_debug = ...
_log = ...

class DetectionMonitor:
    """
    An instance of this class is used to associate a property of an
    object to a parameter of a COV algorithm.  The property_change()
    function is called when the property changes value and that
    value is passed along as an attribute of the algorithm.
    """

    _debug: Callable[..., None]
    def __init__(self, algorithm, parameter, obj, prop, filter=...) -> None: ...
    def property_change(self, old_value, new_value):  # -> None:
        ...

def monitor_filter(parameter):  # -> Callable[..., Any]:
    ...

class DetectionAlgorithm:
    _debug: Callable[..., None]
    _monitors: List[DetectionMonitor]
    _execute_handle: asyncio.Handle
    def __init__(self) -> None: ...
    def bind(self, **kwargs):  # -> None:
        ...
    def unbind(self):  # -> None:
        ...
    def execute(self): ...

class COVDetection(DetectionAlgorithm):
    properties_tracked = ...
    properties_reported = ...
    monitored_property_reference = ...
    def __init__(self, obj) -> None: ...
    def add_subscription(self, cov) -> None: ...
    def cancel_subscription(self, cov) -> None: ...
    def execute(self) -> None:
        """
        By default if one of the properties that are being tracked have changed
        then send out COV notifications to all of the active subscriptions.
        """
        ...

    def send_cov_notifications(self, subscription=...) -> None:
        """
        Send out COV notifications to a specific subscription when it has
        newly joined, or all of the active subscriptions.
        """
        ...

class GenericCriteria(COVDetection):
    properties_tracked = ...
    properties_reported = ...
    monitored_property_reference = ...

class COVIncrementCriteria(COVDetection):
    properties_tracked = ...
    properties_reported = ...
    monitored_property_reference = ...
    def __init__(self, obj) -> None: ...
    @monitor_filter("presentValue")
    def present_value_filter(self, old_value, new_value) -> bool: ...
    def send_cov_notifications(self, subscription=...):  # -> None:
        ...

class AccessDoorCriteria(COVDetection):
    properties_tracked = ...
    properties_reported = ...

class AccessPointCriteria(COVDetection):
    properties_tracked = ...
    properties_reported = ...
    monitored_property_reference = ...

class CredentialDataInputCriteria(COVDetection):
    properties_tracked = ...
    properties_reported = ...

class LoadControlCriteria(COVDetection):
    properties_tracked = ...
    properties_reported = ...

class PulseConverterCriteria(COVIncrementCriteria):
    properties_tracked = ...
    properties_reported = ...
    def __init__(self, obj) -> None: ...
    def add_subscription(self, cov):  # -> None:
        ...
    def cancel_subscription(self, cov):  # -> None:
        ...
    @monitor_filter("covPeriod")
    def cov_period_filter(self, old_value, new_value) -> bool: ...
    def send_cov_notifications(self, subscription=...):  # -> None:
        ...

criteria_type_map = ...
