"""Represent a value that's part integer, part bitfield."""
from __future__ import annotations

import enum
from typing import Mapping

import aenum


class IntWithFlags(enum.IntEnum):
    _flags_: Mapping[str, int]

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls._flags_ = {}

    @classmethod
    def _decompose(cls, value: int) -> tuple[int, list[tuple[str, int]]]:
        flags: list[tuple[str, int]] = []
        for name, flag in getattr(cls, '_flags_', {}).items():
            if value & flag == flag:
                flags.append((name, flag))
                value &= ~flag
        return value, flags

    @classmethod
    def _missing_(cls, value: int) -> enum.IntEnum | None:
        int_value, flags = cls._decompose(value)
        for match_name, match_value in cls.__members__.items():
            if match_value == int_value:
                break
        else:
            return None

        flag_names = [f[0] for f in flags]
        aenum.extend_enum(cls, '|'.join([match_name] + flag_names), (value, ))
        return list(cls)[-1]

    def __or__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        return self.__class__(self._value_ | other)

    __ror__ = __or__
