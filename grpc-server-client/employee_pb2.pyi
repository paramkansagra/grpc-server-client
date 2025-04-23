from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class void(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Employee(_message.Message):
    __slots__ = ("id", "name", "salary")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SALARY_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    salary: float
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., salary: _Optional[float] = ...) -> None: ...

class Employees(_message.Message):
    __slots__ = ("employees",)
    EMPLOYEES_FIELD_NUMBER: _ClassVar[int]
    employees: _containers.RepeatedCompositeFieldContainer[Employee]
    def __init__(self, employees: _Optional[_Iterable[_Union[Employee, _Mapping]]] = ...) -> None: ...
