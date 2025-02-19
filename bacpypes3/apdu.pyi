"""
This type stub file was generated by pyright.
"""

from typing import Callable, Tuple
from .constructeddata import Sequence
from .debugging import bacpypes_debugging
from .pdu import PCI, PDU, PDUData
from .primitivedata import Enumerated

"""
Application Layer Protocol Data Units
"""
_debug = ...
_log = ...
apdu_types = ...
def register_apdu_type(class_):
    ...

confirmed_request_types = ...
def register_confirmed_request_type(class_):
    ...

complex_ack_types = ...
def register_complex_ack_type(class_):
    ...

unconfirmed_request_types = ...
def register_unconfirmed_request_type(class_):
    ...

error_types = ...
def register_error_type(class_):
    ...

class AbortReason(Enumerated):
    _vendor_range = ...
    other = ...
    bufferOverflow = ...
    invalidApduInThisState = ...
    preemptedByHigherPriorityTask = ...
    segmentationNotSupported = ...
    securityError = ...
    insufficientSecurity = ...
    windowSizeOutOfRange = ...
    applicationExceededReplyTime = ...
    outOfResources = ...
    tsmTimeout = ...
    apduTooLong = ...
    serverTimeout = ...
    noResponse = ...


class RejectReason(Enumerated):
    _vendor_range = ...
    other = ...
    bufferOverflow = ...
    inconsistentParameters = ...
    invalidParameterDatatype = ...
    invalidTag = ...
    missingRequiredParameter = ...
    parameterOutOfRange = ...
    tooManyArguments = ...
    undefinedEnumeration = ...
    unrecognizedService = ...


_max_segments_accepted_encoding = ...
def encode_max_segments_accepted(arg): # -> int:
    """Encode the maximum number of segments the device will accept, Section
    20.1.2.4, and if the device says it can only accept one segment it shouldn't
    say that it supports segmentation!"""
    ...

def decode_max_segments_accepted(arg):
    """Decode the maximum number of segments the device will accept, Section
    20.1.2.4"""
    ...

_max_apdu_length_encoding = ...
def encode_max_apdu_length_accepted(arg): # -> int:
    """Return the encoding of the highest encodable value less than the
    value of the arg."""
    ...

def decode_max_apdu_length_accepted(arg):
    ...

@bacpypes_debugging
class APCI(PCI):
    _debug: Callable[..., None]
    _debug_contents: Tuple[str, ...] = ...
    apduType: int
    apduSeg: int
    apduMor: int
    apduSA: int
    apduSrv: int
    apduNak: int
    apduSeq: int
    apduWin: int
    apduMaxSegs: int
    apduMaxResp: int
    apduService: int
    apduInvokeID: int
    apduAbortRejectReason: int
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    def update(self, apci: APCI) -> None:
        ...
    
    def __repr__(self) -> str:
        """Return a string representation of the PDU."""
        ...
    
    def encode(self) -> PDU:
        """encode the contents of the APCI into a PDU."""
        ...
    
    @classmethod
    def decode(class_, pdu: PDU) -> APCI:
        """decode the contents of the PDU and return an APCI."""
        ...
    
    def apci_contents(self, use_dict=..., as_class=...) -> dict:
        """Return the contents of an object as a dict."""
        ...
    


@bacpypes_debugging
class APDU(APCI, PDUData):
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    def set_context(self, context): # -> None:
        """
        This function is called to set the PCI fields to be the response (simple
        ack, complex ack, error, or reject) of a confirmed service request.
        """
        ...
    
    def encode(self) -> PDU:
        ...
    
    @classmethod
    def decode(class_, pdu: PDU) -> APDU:
        ...
    
    def apdu_contents(self, use_dict=..., as_class=...) -> dict:
        ...
    
    def dict_contents(self, use_dict=..., as_class=...) -> dict:
        """Return the contents of an object as a dict."""
        ...
    
    debug_contents = ...


class ConfirmedServiceChoice(Enumerated):
    acknowledgeAlarm = ...
    addListElement = ...
    atomicReadFile = ...
    atomicWriteFile = ...
    auditLogQuery = ...
    authenticate = ...
    confirmedAuditNotification = ...
    confirmedCOVNotification = ...
    confirmedCOVNotificationMultiple = ...
    confirmedEventNotification = ...
    confirmedPrivateTransfer = ...
    confirmedTextMessage = ...
    createObject = ...
    deleteObject = ...
    deviceCommunicationControl = ...
    getAlarmSummary = ...
    getEnrollmentSummary = ...
    getEventInformation = ...
    lifeSafetyOperation = ...
    readProperty = ...
    readPropertyMultiple = ...
    readPropertyConditional = ...
    readRange = ...
    reinitializeDevice = ...
    removeListElement = ...
    requestKey = ...
    subscribeCOV = ...
    subscribeCOVProperty = ...
    subscribeCOVPropertyMultiple = ...
    vtClose = ...
    vtData = ...
    vtOpen = ...
    writeProperty = ...
    writePropertyMultiple = ...


@bacpypes_debugging
@register_apdu_type
class ConfirmedRequestPDU(APDU):
    pduType = ...
    def __init__(self, service_choice=..., invoke_id=..., *args, **kwargs) -> None:
        ...
    


class UnconfirmedServiceChoice(Enumerated):
    iAm = ...
    iHave = ...
    unconfirmedCOVNotification = ...
    unconfirmedEventNotification = ...
    unconfirmedPrivateTransfer = ...
    unconfirmedTextMessage = ...
    timeSynchronization = ...
    whoHas = ...
    whoIs = ...
    utcTimeSynchronization = ...
    writeGroup = ...
    unconfirmedCOVNotificationMultiple = ...
    unconfirmedAuditNotification = ...
    whoIAm = ...
    youAre = ...


@bacpypes_debugging
@register_apdu_type
class UnconfirmedRequestPDU(APDU):
    pduType = ...
    def __init__(self, service_choice=..., *args, **kwargs) -> None:
        ...
    


@bacpypes_debugging
@register_apdu_type
class SimpleAckPDU(APDU):
    pduType = ...
    def __init__(self, service_choice=..., invoke_id=..., context=..., *args, **kwargs) -> None:
        ...
    


@bacpypes_debugging
@register_apdu_type
class ComplexAckPDU(APDU):
    pduType = ...
    def __init__(self, service_choice=..., invoke_id=..., context=..., *args, **kwargs) -> None:
        ...
    


@bacpypes_debugging
@register_apdu_type
class SegmentAckPDU(APDU):
    pduType = ...
    def __init__(self, nak=..., srv=..., invoke_id=..., sequenceNumber=..., windowSize=..., *args, **kwargs) -> None:
        ...
    


class ErrorRejectAbortNack(BaseException):
    """This is a pure virtual class inherited by ErrorPDU, RejectPDU, and
    AbortPDU to make it easier for application layer services to treat them
    all the same.
    """
    @property
    def reason(self) -> int:
        ...
    
    def __str__(self) -> str:
        ...
    


@bacpypes_debugging
@register_apdu_type
class ErrorPDU(APDU, ErrorRejectAbortNack):
    pduType = ...
    def __init__(self, service_choice=..., invoke_id=..., context=..., *args, **kwargs) -> None:
        ...
    


@bacpypes_debugging
@register_apdu_type
class RejectPDU(APDU, ErrorRejectAbortNack):
    pduType = ...
    def __init__(self, invoke_id=..., reason=..., context=..., *args, **kwargs) -> None:
        ...
    


@bacpypes_debugging
@register_apdu_type
class AbortPDU(APDU, ErrorRejectAbortNack):
    pduType = ...
    def __init__(self, srv=..., invoke_id=..., reason=..., context=..., *args, **kwargs) -> None:
        ...
    


@bacpypes_debugging
class APCISequence(APCI, Sequence):
    def __init__(self, **kwargs) -> None:
        ...
    
    def encode(self) -> APDU:
        ...
    
    @classmethod
    def decode(class_, apdu) -> APCISequence:
        ...
    
    def apdu_contents(self, use_dict=..., as_class=...): # -> dict[Any, Any]:
        """Return the contents of an object as a dict."""
        ...
    


@bacpypes_debugging
class ConfirmedRequestSequence(APCISequence, ConfirmedRequestPDU):
    service_choice: int
    def __init__(self, *args, **kwargs) -> None:
        ...
    


@bacpypes_debugging
class ComplexAckSequence(APCISequence, ComplexAckPDU):
    service_choice: int
    def __init__(self, *args, **kwargs) -> None:
        ...
    


@bacpypes_debugging
class UnconfirmedRequestSequence(APCISequence, UnconfirmedRequestPDU):
    service_choice: int
    def __init__(self, *args, **kwargs) -> None:
        ...
    


@bacpypes_debugging
class ErrorSequence(APCISequence, ErrorPDU):
    service_choice: int
    def __init__(self, *args, **kwargs) -> None:
        ...
    


@register_confirmed_request_type
class AcknowledgeAlarmRequest(ConfirmedRequestSequence):
    service_choice = ...
    _order = ...
    acknowledgingProcessIdentifier = ...
    eventObjectIdentifier = ...
    eventStateAcknowledged = ...
    timeStamp = ...
    acknowledgmentSource = ...
    timeOfAcknowledgment = ...


@register_confirmed_request_type
class AddListElementRequest(ConfirmedRequestSequence):
    service_choice = ...
    _order = ...
    objectIdentifier = ...
    propertyIdentifier = ...
    propertyArrayIndex = ...
    listOfElements = ...


@register_confirmed_request_type
class AtomicReadFileRequest(ConfirmedRequestSequence):
    service_choice = ...
    _order = ...
    fileIdentifier = ...
    accessMethod = ...


@register_confirmed_request_type
class AtomicWriteFileRequest(ConfirmedRequestSequence):
    service_choice = ...
    _order = ...
    fileIdentifier = ...
    accessMethod = ...


@register_confirmed_request_type
class AuthenticateRequest(ConfirmedRequestSequence):
    service_choice = ...
    _order = ...
    pseudoRandomNumber = ...
    expectedInvokeID = ...
    operatorName = ...
    operatorPassword = ...
    startEncipheredSession = ...


@register_confirmed_request_type
class ConfirmedCOVNotificationRequest(ConfirmedRequestSequence):
    service_choice = ...
    _order = ...
    subscriberProcessIdentifier = ...
    initiatingDeviceIdentifier = ...
    monitoredObjectIdentifier = ...
    timeRemaining = ...
    listOfValues = ...


@register_confirmed_request_type
class ConfirmedEventNotificationRequest(ConfirmedRequestSequence):
    service_choice = ...
    _order = ...
    processIdentifier = ...
    initiatingDeviceIdentifier = ...
    eventObjectIdentifier = ...
    timeStamp = ...
    notificationClass = ...
    priority = ...
    eventType = ...
    messageText = ...
    notifyType = ...
    ackRequired = ...
    fromState = ...
    toState = ...
    eventValues = ...


@register_confirmed_request_type
class ConfirmedPrivateTransferRequest(ConfirmedRequestSequence):
    service_choice = ...
    _order = ...
    vendorID = ...
    serviceNumber = ...
    serviceParameters = ...


@register_confirmed_request_type
class ConfirmedTextMessageRequest(ConfirmedRequestSequence):
    service_choice = ...
    _order = ...
    textMessageSourceDevice = ...
    messageClass = ...
    messagePriority = ...
    message = ...


@register_confirmed_request_type
class CreateObjectRequest(ConfirmedRequestSequence):
    service_choice = ...
    _order = ...
    objectSpecifier = ...
    listOfInitialValues = ...


@register_confirmed_request_type
class DeleteObjectRequest(ConfirmedRequestSequence):
    service_choice = ...
    _order = ...
    objectIdentifier = ...


@register_confirmed_request_type
class DeviceCommunicationControlRequest(ConfirmedRequestSequence):
    service_choice = ...
    _order = ...
    timeDuration = ...
    enableDisable = ...
    password = ...


@register_confirmed_request_type
class GetAlarmSummaryRequest(ConfirmedRequestSequence):
    service_choice = ...
    _order = ...


@register_confirmed_request_type
class GetEnrollmentSummaryRequest(ConfirmedRequestSequence):
    service_choice = ...
    _order = ...
    acknowledgmentFilter = ...
    enrollmentFilter = ...
    eventStateFilter = ...
    eventTypeFilter = ...
    priorityFilter = ...
    notificationClassFilter = ...


@register_confirmed_request_type
class GetEventInformationRequest(ConfirmedRequestSequence):
    service_choice = ...
    _order = ...
    lastReceivedObjectIdentifier = ...


@register_confirmed_request_type
class LifeSafetyOperationRequest(ConfirmedRequestSequence):
    service_choice = ...
    _order = ...
    requestingProcessIdentifier = ...
    requestingSource = ...
    request = ...
    objectIdentifier = ...


@register_confirmed_request_type
class ReadPropertyMultipleRequest(ConfirmedRequestSequence):
    service_choice = ...
    _order = ...
    listOfReadAccessSpecs = ...


@register_confirmed_request_type
class ReadPropertyRequest(ConfirmedRequestSequence):
    service_choice = ...
    _order = ...
    objectIdentifier = ...
    propertyIdentifier = ...
    propertyArrayIndex = ...


@register_confirmed_request_type
class ReadRangeRequest(ConfirmedRequestSequence):
    service_choice = ...
    _order = ...
    objectIdentifier = ...
    propertyIdentifier = ...
    propertyArrayIndex = ...
    range = ...


@register_confirmed_request_type
class ReinitializeDeviceRequest(ConfirmedRequestSequence):
    service_choice = ...
    _order = ...
    reinitializedStateOfDevice = ...
    password = ...


@register_confirmed_request_type
class RemoveListElementRequest(ConfirmedRequestSequence):
    service_choice = ...
    _order = ...
    objectIdentifier = ...
    propertyIdentifier = ...
    propertyArrayIndex = ...
    listOfElements = ...


@register_confirmed_request_type
class RequestKeyRequest(ConfirmedRequestSequence):
    service_choice = ...
    _order = ...
    requestingDeviceIdentifier = ...
    requestingDeviceAddress = ...
    remoteDeviceIdentifier = ...
    remoteDeviceAddress = ...


@register_confirmed_request_type
class SubscribeCOVPropertyRequest(ConfirmedRequestSequence):
    service_choice = ...
    _order = ...
    subscriberProcessIdentifier = ...
    monitoredObjectIdentifier = ...
    issueConfirmedNotifications = ...
    lifetime = ...
    monitoredPropertyIdentifier = ...
    covIncrement = ...


@register_confirmed_request_type
class SubscribeCOVRequest(ConfirmedRequestSequence):
    service_choice = ...
    _order = ...
    subscriberProcessIdentifier = ...
    monitoredObjectIdentifier = ...
    issueConfirmedNotifications = ...
    lifetime = ...


@register_confirmed_request_type
class VTCloseRequest(ConfirmedRequestSequence):
    service_choice = ...
    _order = ...
    listOfRemoteVTSessionIdentifiers = ...


@register_confirmed_request_type
class VTDataRequest(ConfirmedRequestSequence):
    service_choice = ...
    _order = ...
    vtSessionIdentifier = ...
    vtNewData = ...
    vtDataFlag = ...


@register_confirmed_request_type
class VTOpenRequest(ConfirmedRequestSequence):
    service_choice = ...
    _order = ...
    vtClass = ...
    localVTSessionIdentifier = ...


@register_confirmed_request_type
class WritePropertyMultipleRequest(ConfirmedRequestSequence):
    service_choice = ...
    _order = ...
    listOfWriteAccessSpecs = ...


@register_confirmed_request_type
class WritePropertyRequest(ConfirmedRequestSequence):
    service_choice = ...
    _order = ...
    objectIdentifier = ...
    propertyIdentifier = ...
    propertyArrayIndex = ...
    propertyValue = ...
    priority = ...


@register_unconfirmed_request_type
class IAmRequest(UnconfirmedRequestSequence):
    service_choice = ...
    _order = ...
    iAmDeviceIdentifier = ...
    maxAPDULengthAccepted = ...
    segmentationSupported = ...
    vendorID = ...


@register_unconfirmed_request_type
class IHaveRequest(UnconfirmedRequestSequence):
    service_choice = ...
    _order = ...
    deviceIdentifier = ...
    objectIdentifier = ...
    objectName = ...


@register_unconfirmed_request_type
class TimeSynchronizationRequest(UnconfirmedRequestSequence):
    service_choice = ...
    _order = ...
    time = ...


@register_unconfirmed_request_type
class UTCTimeSynchronizationRequest(UnconfirmedRequestSequence):
    service_choice = ...
    _order = ...
    time = ...


@register_unconfirmed_request_type
class UnconfirmedCOVNotificationRequest(UnconfirmedRequestSequence):
    service_choice = ...
    _order = ...
    subscriberProcessIdentifier = ...
    initiatingDeviceIdentifier = ...
    monitoredObjectIdentifier = ...
    timeRemaining = ...
    listOfValues = ...


@register_unconfirmed_request_type
class UnconfirmedEventNotificationRequest(UnconfirmedRequestSequence):
    service_choice = ...
    _order = ...
    processIdentifier = ...
    initiatingDeviceIdentifier = ...
    eventObjectIdentifier = ...
    timeStamp = ...
    notificationClass = ...
    priority = ...
    eventType = ...
    messageText = ...
    notifyType = ...
    ackRequired = ...
    fromState = ...
    toState = ...
    eventValues = ...


@register_unconfirmed_request_type
class UnconfirmedPrivateTransferRequest(UnconfirmedRequestSequence):
    service_choice = ...
    _order = ...
    vendorID = ...
    serviceNumber = ...
    serviceParameters = ...


@register_unconfirmed_request_type
class UnconfirmedTextMessageRequest(UnconfirmedRequestSequence):
    service_choice = ...
    _order = ...
    textMessageSourceDevice = ...
    messageClass = ...
    messagePriority = ...
    message = ...


@register_unconfirmed_request_type
class WhoHasRequest(UnconfirmedRequestSequence):
    service_choice = ...
    _order = ...
    limits = ...
    object = ...


@register_unconfirmed_request_type
class WhoIsRequest(UnconfirmedRequestSequence):
    service_choice = ...
    _order = ...
    deviceInstanceRangeLowLimit = ...
    deviceInstanceRangeHighLimit = ...


@register_unconfirmed_request_type
class WriteGroupRequest(UnconfirmedRequestSequence):
    service_choice = ...
    _order = ...
    groupNumber = ...
    writePriority = ...
    changeList = ...
    inhibitDelay = ...


@register_complex_ack_type
class AtomicReadFileACK(ComplexAckSequence):
    service_choice = ...
    _order = ...
    endOfFile = ...
    accessMethod = ...


@register_complex_ack_type
class AtomicWriteFileACK(ComplexAckSequence):
    service_choice = ...
    _order = ...
    fileStartPosition = ...
    fileStartRecord = ...


@register_complex_ack_type
class AuthenticateACK(ComplexAckSequence):
    service_choice = ...
    _order = ...
    modifiedRandomNumber = ...


@register_complex_ack_type
class ConfirmedPrivateTransferACK(ComplexAckSequence):
    service_choice = ...
    _order = ...
    vendorID = ...
    serviceNumber = ...
    resultBlock = ...


@register_complex_ack_type
class CreateObjectACK(ComplexAckSequence):
    service_choice = ...
    _order = ...
    objectIdentifier = ...


@register_complex_ack_type
class GetAlarmSummaryACK(ComplexAckSequence):
    service_choice = ...
    _order = ...
    listOfAlarmSummaries = ...


@register_complex_ack_type
class GetEnrollmentSummaryACK(ComplexAckSequence):
    service_choice = ...
    _order = ...
    listOfEnrollmentSummaries = ...


@register_complex_ack_type
class GetEventInformationACK(ComplexAckSequence):
    service_choice = ...
    _order = ...
    listOfEventSummaries = ...
    moreEvents = ...


@register_complex_ack_type
class ReadPropertyACK(ComplexAckSequence):
    service_choice = ...
    _order = ...
    objectIdentifier = ...
    propertyIdentifier = ...
    propertyArrayIndex = ...
    propertyValue = ...


@register_complex_ack_type
class ReadPropertyMultipleACK(ComplexAckSequence):
    service_choice = ...
    _order = ...
    listOfReadAccessResults = ...


@register_complex_ack_type
class ReadRangeACK(ComplexAckSequence):
    service_choice = ...
    _order = ...
    objectIdentifier = ...
    propertyIdentifier = ...
    propertyArrayIndex = ...
    resultFlags = ...
    itemCount = ...
    itemData = ...
    firstSequenceNumber = ...


@register_complex_ack_type
class VTDataACK(ComplexAckSequence):
    service_choice = ...
    _order = ...
    allNewDataAccepted = ...
    acceptedOctetCount = ...


@register_complex_ack_type
class VTOpenACK(ComplexAckSequence):
    service_choice = ...
    _order = ...
    remoteVTSessionIdentifier = ...


class Error(ErrorSequence):
    _order = ...
    errorClass = ...
    errorCode = ...
    def __str__(self) -> str:
        ...
    


class ChangeListError(ErrorSequence):
    _order = ...
    errorType = ...
    firstFailedElementNumber = ...


@register_error_type
class ConfirmedPrivateTransferError(ErrorSequence):
    service_choice = ...
    _order = ...
    errorType = ...
    vendorID = ...
    serviceNumber = ...
    errorParameters = ...


@register_error_type
class CreateObjectError(ErrorSequence):
    service_choice = ...
    _order = ...
    errorType = ...
    firstFailedElementNumber = ...


@register_error_type
class VTCloseError(ErrorSequence):
    service_choice = ...
    _order = ...
    errorType = ...
    listOfVTSessionIdentifiers = ...


@register_error_type
class WritePropertyMultipleError(ErrorSequence):
    service_choice = ...
    _order = ...
    errorType = ...
    firstFailedWriteAttempt = ...


