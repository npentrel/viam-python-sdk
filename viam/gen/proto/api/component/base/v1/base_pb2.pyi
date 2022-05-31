"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
from ...... import proto
import typing
import typing_extensions
DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class MoveStraightRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    DISTANCE_MM_FIELD_NUMBER: builtins.int
    MM_PER_SEC_FIELD_NUMBER: builtins.int
    name: typing.Text
    'Name of a base'
    distance_mm: builtins.int
    'Desired travel distance in millimeters'
    mm_per_sec: builtins.float
    'Desired travel velocity in millimeters/second'

    def __init__(self, *, name: typing.Text=..., distance_mm: builtins.int=..., mm_per_sec: builtins.float=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['distance_mm', b'distance_mm', 'mm_per_sec', b'mm_per_sec', 'name', b'name']) -> None:
        ...
global___MoveStraightRequest = MoveStraightRequest

class MoveStraightResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(self) -> None:
        ...
global___MoveStraightResponse = MoveStraightResponse

class SpinRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    ANGLE_DEG_FIELD_NUMBER: builtins.int
    DEGS_PER_SEC_FIELD_NUMBER: builtins.int
    name: typing.Text
    'Name of a base'
    angle_deg: builtins.float
    'Desired angle'
    degs_per_sec: builtins.float
    'Desired angular velocity'

    def __init__(self, *, name: typing.Text=..., angle_deg: builtins.float=..., degs_per_sec: builtins.float=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['angle_deg', b'angle_deg', 'degs_per_sec', b'degs_per_sec', 'name', b'name']) -> None:
        ...
global___SpinRequest = SpinRequest

class SpinResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(self) -> None:
        ...
global___SpinResponse = SpinResponse

class StopRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text
    'Name of a base'

    def __init__(self, *, name: typing.Text=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['name', b'name']) -> None:
        ...
global___StopRequest = StopRequest

class StopResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(self) -> None:
        ...
global___StopResponse = StopResponse

class SetPowerRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    LINEAR_FIELD_NUMBER: builtins.int
    ANGULAR_FIELD_NUMBER: builtins.int
    name: typing.Text
    'Name of a base'

    @property
    def linear(self) -> proto.api.common.v1.common_pb2.Vector3:
        """Desired linear power percentage as -1 -> 1"""
        pass

    @property
    def angular(self) -> proto.api.common.v1.common_pb2.Vector3:
        """Desired angular power percentage % as -1 -> 1"""
        pass

    def __init__(self, *, name: typing.Text=..., linear: typing.Optional[proto.api.common.v1.common_pb2.Vector3]=..., angular: typing.Optional[proto.api.common.v1.common_pb2.Vector3]=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['angular', b'angular', 'linear', b'linear']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['angular', b'angular', 'linear', b'linear', 'name', b'name']) -> None:
        ...
global___SetPowerRequest = SetPowerRequest

class SetPowerResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(self) -> None:
        ...
global___SetPowerResponse = SetPowerResponse

class SetVelocityRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    LINEAR_FIELD_NUMBER: builtins.int
    ANGULAR_FIELD_NUMBER: builtins.int
    name: typing.Text
    'Name of a base'

    @property
    def linear(self) -> proto.api.common.v1.common_pb2.Vector3:
        """Desired linear velocity in mm per second"""
        pass

    @property
    def angular(self) -> proto.api.common.v1.common_pb2.Vector3:
        """Desired angular velocity in degrees per second"""
        pass

    def __init__(self, *, name: typing.Text=..., linear: typing.Optional[proto.api.common.v1.common_pb2.Vector3]=..., angular: typing.Optional[proto.api.common.v1.common_pb2.Vector3]=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['angular', b'angular', 'linear', b'linear']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['angular', b'angular', 'linear', b'linear', 'name', b'name']) -> None:
        ...
global___SetVelocityRequest = SetVelocityRequest

class SetVelocityResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(self) -> None:
        ...
global___SetVelocityResponse = SetVelocityResponse