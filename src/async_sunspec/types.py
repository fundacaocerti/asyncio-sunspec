# *****************************************************************************
# Copyright (c) 2026 CERTI Foundation.
#
# This Source Code Form is subject to the terms of the Mozilla Public 
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# *****************************************************************************
"""Implement type encoders/decoders used by SunSpec points."""

from __future__ import annotations

import struct
from abc import ABC, abstractmethod
from array import array
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class SunSpecType(ABC):
    """Describe conversion rules between typed values and register slices."""

    default: Any
    not_implemented: Any
    size: int

    @abstractmethod
    def validate(self, val: Any) -> bool:
        """Return whether a value is valid for this SunSpec type.

        Args:
            val: The value to validate.

        Returns:
            ``True`` if ``val`` is acceptable, ``False`` otherwise.
        """
        pass

    @abstractmethod
    def into_register(self, value: Any, register: array | memoryview) -> None:
        """Encode ``value`` into a mutable register slice.

        Args:
            value: The typed value to encode.
            register: A writable ``array`` or ``memoryview`` of the correct
                size for this type.
        """
        pass

    @abstractmethod
    def from_register(self, register: array | memoryview) -> Any:
        """Decode a typed value from a register slice.

        Args:
            register: A readable ``array`` or ``memoryview`` of the correct
                size for this type.

        Returns:
            The decoded typed value.
        """
        pass

@dataclass(frozen=True)
class SunSpecTypeNumeral[T](SunSpecType):
    """Encode and decode bounded numeric values using ``struct`` formats."""

    lower_bound: int
    upper_bound: int
    type_code: str

    def validate(self, value: T) -> bool:
        """Check if a numeric value falls within configured bounds.

        Args:
            value: The numeric value to check.

        Returns:
            ``True`` if ``value`` equals ``not_implemented`` or lies within
            ``[lower_bound, upper_bound]``, ``False`` otherwise.
        """
        if value == self.not_implemented:
            return True
        elif self.lower_bound is not None and value < self.lower_bound:
            return False
        elif self.upper_bound is not None and value > self.upper_bound:
            return False
        return True

    def into_register(self, value: T, register: array | memoryview) -> None:
        """Pack a numeric value into 16-bit register words.

        Args:
            value: The numeric value to encode.
            register: A writable ``array`` or ``memoryview`` of
                :attr:`size` slots.

        Raises:
            ValueError: If ``value`` fails :meth:`validate`.
        """
        if not self.validate(value):
            raise ValueError(f"Value {value} is out of {self.__class__.__name__} bounds [{self.lower_bound}, {self.upper_bound}]")
        packed = struct.pack(f'>{self.type_code}', value)
        unpacked = struct.unpack(f'>{self.size}H', packed)
        for i in range(self.size):
            register[i] = unpacked[i]
    
    def from_register(self, register: array | memoryview) -> T:
        """Unpack a numeric value from 16-bit register words.

        Args:
            register: A readable ``array`` or ``memoryview`` of
                :attr:`size` slots.

        Returns:
            The decoded numeric value.
        """
        packed = struct.pack(f'>{self.size}H', *register[:self.size])
        unpacked = struct.unpack(f'>{self.type_code}', packed)
        value = unpacked[0]
        return value
    
@dataclass(frozen=True)
class SunSpecTypeString(SunSpecType):
    """Encode and decode fixed-size ASCII-like SunSpec strings."""

    def validate(self, val: str) -> bool:
        """Return whether ``val`` is a Python string.

        Args:
            val: The value to validate.

        Returns:
            ``True`` if ``val`` is a ``str`` instance.
        """
        return isinstance(val, str)

    def into_register(self, value: str, register: array | memoryview) -> None:
        """Write one character per register and null-pad remaining slots.

        Each register word holds the ordinal of one ASCII character.  Slots
        beyond ``len(value)`` are zeroed.

        Args:
            value: The string to encode.  Must not exceed ``len(register)``
                characters.
            register: A writable ``array`` or ``memoryview`` of at least
                ``len(value)`` slots.

        Raises:
            TypeError: If ``value`` is not a ``str``.
            ValueError: If ``value`` is longer than ``register``.
        """
        if not self.validate(value):
            raise TypeError(f"Expected str, got {type(value).__name__}")
        
        if len(value) > len(register):
            raise ValueError("String too long to fit in register!")

        for i, char in enumerate(value):
            register[i] = ord(char)
        for j in range(len(value), len(register)):
            register[j] = 0x00
    
    def from_register(self, register: array | memoryview) -> str:
        """Read characters until the first null register or buffer end.

        Args:
            register: A readable ``array`` or ``memoryview`` of any size.

        Returns:
            The decoded string, stopping at the first ``0x00`` slot.
        """
        chars = []
        for val in register:
            if val == 0x00:
                break
            chars.append(chr(val))
        return ''.join(chars)

FLOAT = SunSpecTypeNumeral[float](lower_bound=None, upper_bound=None, type_code='f', size=2, default=0.0, not_implemented=0xFFFFFFFF)
"""IEEE 754 single-precision float mapped to 2 registers (``float32``)."""
UINT16 = SunSpecTypeNumeral[int](lower_bound=0, upper_bound=2**16-1, type_code='H', size=1, default=0, not_implemented=0xFFFF)
"""Unsigned 16-bit integer, 1 register.  Not-implemented sentinel: ``0xFFFF``."""
UINT32 = SunSpecTypeNumeral[int](lower_bound=0, upper_bound=2**32-1, type_code='I', size=2, default=0, not_implemented=0xFFFFFFFF)
"""Unsigned 32-bit integer, 2 registers."""
UINT64 = SunSpecTypeNumeral[int](lower_bound=0, upper_bound=2**64-1, type_code='Q', size=4, default=0, not_implemented=0xFFFFFFFFFFFFFFFF)
"""Unsigned 64-bit integer, 4 registers."""
INT16 = SunSpecTypeNumeral[int](lower_bound=-2**15, upper_bound=2**15-1, type_code='h', size=1, default=0, not_implemented=-(2**15))
"""Signed 16-bit integer, 1 register."""
INT32 = SunSpecTypeNumeral[int](lower_bound=-2**31, upper_bound=2**31-1, type_code='i', size=2, default=0, not_implemented=-(2**31))
"""Signed 32-bit integer, 2 registers."""
INT64 = SunSpecTypeNumeral[int](lower_bound=-2**63, upper_bound=2**63-1, type_code='q', size=4, default=0, not_implemented=-(2**63))
"""Signed 64-bit integer, 4 registers."""
SUNSSF = SunSpecTypeNumeral[int](lower_bound=-10, upper_bound=10, type_code='h', size=1, default=0, not_implemented=-(2**15))
"""SunSpec scale-factor exponent in range ``[-10, 10]``, 1 register."""
STRING = SunSpecTypeString(default="", not_implemented="", size=0)
"""Variable-length ASCII string; ``size`` is set per-point at construction."""

TYPE_MAP: dict[str, SunSpecType] = {
    "float32": FLOAT,
    "int16": INT16,
    "int32": INT32,
    "int64": INT64,
    "string": STRING,
    "sunssf": SUNSSF,
    "uint16": UINT16,
    "uint32": UINT32,
    "uint64": UINT64,
}
