"""
This type stub file was generated by pyright.
"""

import asyncio
from threading import Thread
from typing import Any as _Any, Callable, Dict, List, Optional, Tuple, Union
from ..debugging import bacpypes_debugging
from ..primitivedata import CharacterString, ObjectIdentifier
from ..basetypes import PropertyIdentifier
from ..constructeddata import ArrayOf
from ..object import NotificationClassObject, Object as _Object

"""
Local Object
"""
_debug = ...
_log = ...
ExecuteMethod = Callable[["Algorithm"], _Any]
_vendor_id = ...

class PropertyGetterThread(Thread):
    """
    An instance of this class is used when the getter of a property is a
    coroutine function and must run in its own event loop.
    """
    def __init__(self, getattr_fn) -> None: ...
    def run(self):  # -> None:
        ...

class PropertySetterThread(Thread):
    """
    An instance of this class is used when the setter and/or getter of
    a property is a coroutine function and must run in its own event
    loop.
    """
    def __init__(self, getattr_fn, setattr_fn, new_value) -> None: ...
    def run(self):  # -> None:
        ...

class Algorithm:
    """
    This is an abstract superclass of FaultAlgorithm and EventAlgorithm.
    """

    _debug: Callable[..., None]
    _parameters: Dict[str, Parameter]
    _what_changed: Dict[str, Tuple[_Any, _Any]]
    _execute_enabled: bool
    _execute_handle: Optional[asyncio.Handle]
    _execute_fn: ExecuteMethod
    def __init__(self) -> None: ...
    def __getattr__(self, attr: str) -> _Any:
        """
        If attr is a parameter, redirect to the Parameter instance.
        """
        ...

    def __setattr__(self, attr: str, value: _Any) -> None:
        """
        If attr is a parameter, redirect to the Parameter instance.
        """
        ...

    def bind(self, **kwargs):  # -> None:
        ...
    def unbind(self):  # -> None:
        ...
    def init(self):  # -> None:
        """
        This is called after the `bind()` call.
        """
        ...

    def execute(self) -> _Any:
        """
        Using the bound parameters, execute the algorithm.  This should be an
        @abstractmethod at some point.
        """
        ...

class Parameter:
    """
    An instance of this class is used to associate a property of an
    object to a parameter of an event algorithm.  The property_change()
    function is called when the property changes value and that
    value is passed along as an attribute of the algorithm.
    """

    _debug: Callable[..., None]
    algorithm: Algorithm
    parameter_name: str
    obj: Object
    property_identifier: str
    listen: bool
    def __init__(
        self,
        algorithm: Algorithm,
        parameter_name: str,
        obj: Object,
        property_identifier: Union[int, str, PropertyIdentifier],
        listen: Optional[bool] = ...,
    ) -> None: ...
    def getattr(self) -> _Any:
        """
        This function is called when the algoritm needs the value of the
        property from the object.
        """
        ...

    def setattr(self, value: _Any) -> None:
        """
        This function is called when the algorithm updates the value of
        a property from the object.
        """
        ...

    def property_change(self, old_value, new_value):  # -> None:
        ...

class Object(_Object):
    """
    A local object has specialized property functions for changing the object
    name and identifier and has a dynamically generated propertyList property.
    """

    __objectName: CharacterString
    __objectIdentifier: ObjectIdentifier
    _property_monitors: Dict[str, List[Callable[..., None]]]
    _event_algorithm: Optional[Algorithm] = ...
    _fault_algorithm: Optional[Algorithm] = ...
    _notification_class_object: Optional[NotificationClassObject] = ...
    def __init__(self, **kwargs) -> None: ...
    def __getattribute__(self, attr: str) -> _Any: ...
    def __setattr__(self, attr: str, value: _Any) -> None:
        """
        This function traps changes to properties that have at least
        one associated monitor function.
        """
        ...

    @property
    def objectName(self) -> CharacterString:
        """Return the private value of the object name."""
        ...

    @objectName.setter
    def objectName(self, value: CharacterString) -> None:
        """
        Change the object name, and if it is associated with an application,
        update the application reference to this object.
        """
        ...

    @property
    def objectIdentifier(self) -> ObjectIdentifier:
        """
        Return the private value of the object identifier.
        """
        ...

    @objectIdentifier.setter
    def objectIdentifier(self, value: ObjectIdentifier) -> None:
        """
        Change the object identifier, and if it is associated with an
        application, update the application reference to this object.
        """
        ...

    @property
    def propertyList(self) -> ArrayOf(PropertyIdentifier):
        """Return an array of property identifiers."""
        ...

    @propertyList.setter
    def propertyList(self, value: _Any) -> None:
        """
        Change the property list, usually called with None in the case of
        an object being initialized, or in the case when the value is
        unmarshalled from a JSON blob or RDF graph, in both cases it
        can be ignored.
        """
        ...

    @property
    def statusFlags(self) -> ArrayOf(PropertyIdentifier):
        """Return the status flags."""
        ...

    @statusFlags.setter
    def statusFlags(self, value: _Any) -> None:
        """
        Change the status flags, usually called with None in the case of
        an object being initialized, or in the case when the value is
        unmarshalled from a JSON blob or RDF graph, in both cases it
        can be ignored.
        """
        ...
