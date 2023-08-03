import abc

import typing_extensions as te


@te.runtime_checkable
class SupportsStr(te.Protocol):
    __slots__ = ()

    @abc.abstractmethod
    def __str__(self) -> str:
        pass
