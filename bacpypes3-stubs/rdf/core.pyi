"""
This type stub file was generated by pyright.
"""

from typing import Any, Callable, Optional
from rdflib import Graph, URIRef
from rdflib.namespace import Namespace
from ..debugging import bacpypes_debugging
from ..pdu import Address
from ..primitivedata import ObjectIdentifier
from ..basetypes import PropertyIdentifier

"""
Core
"""
_debug = ...
_log = ...
BACnetNS = ...
BACnetURI = ...

def device_node(device_identifier: ObjectIdentifier) -> URIRef:
    """Given a device identifer return a URI reference for the device, the
    default function returns a value from Annex Q.8."""
    ...

def object_node(device_iri: URIRef, object_identifier: ObjectIdentifier) -> URIRef:
    """Given a device IRI for context and an object identifier,
    return a URI reference for the object."""
    ...

def property_node(
    object_iri: URIRef, property_identifier: PropertyIdentifier
) -> URIRef:
    """Given an object IRI for context and a property identifier, return a URI
    reference for the property."""
    ...

def blank_node() -> URIRef:
    """Return a blank node."""
    ...

_device_node: Callable[..., URIRef] = ...
_object_node: Callable[..., URIRef] = ...
_blank_node: Callable[..., URIRef] = ...

def set_identifier_functions(
    *,
    device_node_fn: Callable[..., URIRef] = ...,
    object_node_fn: Callable[..., URIRef] = ...,
    blank_node_fn: Callable[..., URIRef] = ...,
):  # -> None:
    """This function allows the application using the library to provide
    its own functions for contsructing URI node identifiers for
    devices, objects and blank nodes.
    """
    ...

def bacnet_query(query: str) -> Any:
    """Prepare a SPARQL query with the BACnet namespace prefix included.
    The prepared query is provided to the `BACnetGraph.query()` method
    along with initial variable bindings if they have been provided.
    """
    ...

find_device_by_address = ...
find_device_by_instance = ...
find_object_by_type = ...

class BACnetGraph:
    """
    Creates a graph context where BACnet content can be found.
    """

    _debug: Callable[..., None]
    def __init__(self, graph: Graph) -> None: ...
    def bind_namespace(self, prefix: str, uri: str) -> Namespace:
        """
        Create a Namespace and bind a prefix to it in the graph.
        """
        ...

    def query(self, query: Any, **kwargs: Any) -> Any:
        """Run a prepared SPARQL query in the graph with the initial bindings
        and return the results.
        """
        ...

    def create_device(
        self,
        device_address: Optional[Address],
        device_identifier: Optional[ObjectIdentifier],
    ) -> DeviceGraph:
        """Given a device network address or a device identifier (or both)
        create and return a DeviceGraph for the device.
        """
        ...

    def find_device(
        self,
        device_address: Optional[Address] = ...,
        device_identifier: Optional[ObjectIdentifier] = ...,
    ) -> Optional[DeviceGraph]:
        """Given a device network address or a device identifier (or both)
        find the existing DeviceGraph for the device, or return None if
        the device isn't defined.
        """
        ...

    def delete_device(
        self,
        device_address: Optional[Address] = ...,
        device_identifier: Optional[ObjectIdentifier] = ...,
    ) -> None:
        """Given a device network address or a device identifier (or both)
        find the existing DeviceGraph for the device and delete all of its
        associated nodes.
        """
        ...

class DeviceGraph:
    """
    Creates a graph context where BACnet content for a specific device
    can be found.
    """

    _debug: Callable[..., None]
    def __init__(self, graph: BACnetGraph, device_iri: URIRef) -> None: ...
    def create_object(self, object_identifier: ObjectIdentifier) -> ObjectProxy:
        """Given an object identifier return an ObjectProxy for the object."""
        ...

    def find_object(self, object_identifier: ObjectIdentifier) -> Optional[ObjectProxy]:
        """Given an object identifier return an ObjectProxy for the object."""
        ...

    def delete_object(self, object_identifier: ObjectIdentifier) -> None:
        """Given an object identifier find the existing ObjectProxy for the
        object and delete all of its associated nodes.
        """
        ...

class ObjectProxy:
    """
    A proxy for getting and setting property values of an object.
    """

    _debug: Callable[..., None]
    _graph: BACnetGraph
    _object_iri: URIRef
    _object_cls: Optional[type]
    def __init__(
        self, graph: BACnetGraph, object_iri: URIRef, object_cls: Optional[type] = ...
    ) -> None: ...
    def __getattr__(self, attr: str) -> Any: ...
    def __setattr__(self, attr: str, value: Any) -> None: ...
