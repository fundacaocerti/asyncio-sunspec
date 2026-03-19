# *****************************************************************************
# Copyright (c) 2026 CERTI Foundation.
#
# This Source Code Form is subject to the terms of the Mozilla Public 
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# *****************************************************************************
"""Define SunSpec point metadata and register-backed point values."""

from __future__ import annotations

from array import array
from enum import StrEnum
from typing import Any

from .types import TYPE_MAP


class SunSpecPointAccess(StrEnum):
    """Declare allowed access modes for a SunSpec point."""

    RW = "RW"
    R = "R"
    W = "W"


class SunSpecPoint:
    """Represent a single typed SunSpec point bound to holding registers."""

    def __init__(
        self,
        name: str,
        ptype: str,
        *,
        value: Any = None,
        offset: int = None,
        size: int = None,
        mandatory: bool = True,
        static: bool = False,
        access: SunSpecPointAccess = SunSpecPointAccess.R,
    ) -> None:
        """Initialize point metadata and allocate the backing register slice.

        Args:
            name: Human-readable point name used in error messages.
            ptype: SunSpec type string (e.g. ``"uint16"``, ``"float32"``).
            value: Initial typed value.  Defaults to the type's
                ``default`` when ``mandatory=True``, or ``not_implemented``
                otherwise.
            offset: Register offset relative to the parent container.  Set
                later by :meth:`.SunSpecGroup.process_elements`.
            size: Override for the number of 16-bit registers.  Falls back
                to the type's natural size when ``None``.
            mandatory: When ``False`` the point is initialised to its
                ``not_implemented`` sentinel value.  Defaults to ``True``.
            static: Mark the point as immutable after locking.  Static
                points must be read-only (``access=R``).  Defaults to
                ``False``.
            access: Read/write access mode.  Defaults to
                :attr:`SunSpecPointAccess.R`.

        Raises:
            ValueError: If ``static=True`` and ``access`` is not ``R``.
            ValueError: If ``ptype`` is not present in
                :data:`.types.TYPE_MAP`.
            ValueError: If the resolved ``size`` is zero or negative.
        """
        self._name = name
        self._type = ptype
        self._offset = offset
        self._mandatory = mandatory
        self._static = static
        self._access = access
        self._scale_factor: SunSpecPoint | None = None
        self._locked = False

        if not self._access == SunSpecPointAccess.R and static:
            raise ValueError(f"Static point '{self._name}' must be read-only!")
        
        self._validator = TYPE_MAP.get(ptype)
        if self._validator is None:
            raise ValueError(f"Unknown point type '{ptype}' for '{self._name}'")
        self._size = size or self._validator.size
        self._register = array('H', [0] * self._size)

        _default = self._validator.default if mandatory else self._validator.not_implemented
        value = value if value is not None else _default
        self._validator.into_register(value, self._register)

        if not bool(self._size):
            raise ValueError(f"Point size must be a positive integer, got {self._size} for '{self._name}'!")

    @classmethod
    def create(cls, namespace: dict[str, Any], **kwargs) -> SunSpecPoint:
        """Create a point instance from metadata kwargs.

        Args:
            namespace: Parent group namespace (unused by points, passed for
                API symmetry with :meth:`.SunSpecGroup.create`).
            **kwargs: Keyword arguments forwarded to :meth:`__init__`.

        Returns:
            A new :class:`SunSpecPoint` instance.
        """
        return cls(**kwargs)

    @property
    def value(self):
        """Return the typed value decoded from the backing registers."""
        return self._validator.from_register(self._register)
    
    @value.setter
    def value(self, value):
        """Encode and store a typed value into the backing registers."""
        if self._static and self._locked:
            raise AttributeError(f"Cannot modify locked static point '{self._name}'")
        self._validator.into_register(value, self._register)

    @property
    def size(self):
        """Return point size in 16-bit registers."""
        return self._size
    
    @property
    def offset(self):
        """Return point offset relative to its parent container."""
        return self._offset
    
    @offset.setter
    def offset(self, offset: int) -> None:
        """Set point offset relative to its parent container."""
        self._offset = offset
    
    def bind_register(self, register: array | memoryview) -> None:
        """Rebind the point register view while preserving current typed value.

        Decodes the current value first, then calls :meth:`value.setter` to
        re-encode it into ``register``.  Use this method when attaching a
        point to a shared device buffer.

        Args:
            register: A writable ``array`` slice or ``memoryview`` of the
                correct size for this point.
        """
        value = self.value
        self._register = register
        self.value = value

    def read_from_register(self, register: array | memoryview) -> None:
        """Rebind the point register view without re-encoding a value.

        Unlike :meth:`bind_register`, the existing register content is left
        unchanged.  Use this method when reading values from a remote device
        into an already-populated buffer.

        Args:
            register: A ``memoryview`` or ``array`` slice that already
                contains the register data to expose.
        """
        self._register = register

    def bind_scale_factor(self, scale_factor_point: SunSpecPoint) -> None:
        """Attach another point to be used as this point's scale factor.

        The referenced point holds a ``sunssf`` exponent.  Consumers may
        multiply :attr:`value` by ``10 ** scale_factor_point.value`` to
        obtain the engineering value.

        Args:
            scale_factor_point: A :class:`SunSpecPoint` of type ``sunssf``
                whose value provides the decimal exponent.
        """
        self._scale_factor = scale_factor_point
        
    def lock(self) -> bool:
        """Lock point writes and return success.

        Returns:
            Always ``True``.
        """
        self._locked = True
        return True

    def unlock(self) -> bool:
        """Unlock point writes and return success.

        Returns:
            Always ``True``.
        """
        self._locked = False
        return True

    @property
    def is_locked(self) -> bool:
        """Return whether writes are currently locked."""
        return self._locked
