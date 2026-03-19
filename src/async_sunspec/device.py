# *****************************************************************************
# Copyright (c) 2026 CERTI Foundation.
#
# This Source Code Form is subject to the terms of the Mozilla Public 
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# *****************************************************************************
"""Define a SunSpec device container and register layout handling."""

from array import array

from .model import SunSpecModel

SUNSPEC_HEADER = (0x5375, 0x6E53)  # "Su", "ns"
SUNSPEC_END_MODEL = (0xFFFF, 0x0000)  # End

class SunSpecDevice:
    """Aggregate SunSpec models and bind them to a shared register buffer."""

    def __init__(self, device_id: int = 0, address: int = 0) -> None:
        """Initialize device identity, model storage, and register state.

        Args:
            device_id: Modbus device / unit identifier. Defaults to ``0``.
            address: Base holding-register address where the SunSpec header
                (``"SuNs"``) begins. Defaults to ``0``.
        """
        self._device_id = device_id
        self._address = address
        self._sunspec_models: dict[int, SunSpecModel] = {}
        self._length: int = 0
        self._locked = False
        self._register: array | memoryview | None = None

    @property
    def device_id(self) -> int:
        """Return Modbus device ID."""
        return self._device_id

    @property
    def address(self) -> int:
        """Return base register address where SunSpec data starts."""
        return self._address
    
    def add_model(self, model: SunSpecModel) -> None:
        """Attach a model to this device keyed by model ID.

        Args:
            model: The :class:`.SunSpecModel` instance to register.

        Raises:
            ValueError: If a model with the same ID already exists on the
                device.
        """
        if model.id in self._sunspec_models:
            raise ValueError(f"Model with ID {model.id} already exists in device {self._device_id}")
        self._sunspec_models[model.id] = model

    def remove_model(self, model_id: int) -> None:
        """Remove a model from this device by model ID.

        Args:
            model_id: Numeric SunSpec model identifier.

        Raises:
            ValueError: If no model with ``model_id`` is registered.
        """
        if model_id not in self._sunspec_models:
            raise ValueError(f"Model with ID {model_id} does not exist in device {self._device_id}")
        del self._sunspec_models[model_id]

    def process_elements(self) -> int:
        """Compute model offsets and total device register length.

        Returns:
            Total number of 16-bit registers occupied by this device,
            including the 2-register SunSpec header and the 2-register
            end-of-model marker.
        """
        length = 0x02
        for model in self._sunspec_models.values():
            model.offset = length
            model.process_elements()
            length += model.length
        length += 0x02  # End model marker (0xFFFF, 0x0000)
        self._length = length
        return length

    def bind_register(self, register: array | memoryview | None = None) -> None:
        """Bind or create a register buffer and map all models onto it.

        Calls :meth:`process_elements` to recompute all offsets, then slices
        the buffer for each model via :meth:`.SunSpecModel.bind_register`.

        Args:
            register: An existing ``array`` or ``memoryview`` to reuse.  When
                ``None`` (default) a new ``array('H')`` is allocated with the
                correct size.
        """
        self.process_elements()
        self._register = register or array('H', [0] * self._length)

        self._register[0] = SUNSPEC_HEADER[0]  # "Su"
        self._register[1] = SUNSPEC_HEADER[1]  # "ns"
        self._register[-2] = SUNSPEC_END_MODEL[0]  # End model ID
        self._register[-1] = SUNSPEC_END_MODEL[1]  # End model length

        for model in self._sunspec_models.values():
            mview = memoryview(self._register)[model.offset:model.offset + model.length]
            model.bind_register(mview)

    def lock(self) -> bool:
        """Lock all models and freeze current register-facing values.

        Returns:
            ``True`` if every model locked successfully, ``False`` if any
            model refused to lock.
        """
        for model in self._sunspec_models.values():
            if not model.lock():
                return False
        
        self._locked = True
        return True
    
    def unlock(self) -> bool:
        """Unlock all models to allow further updates.

        Returns:
            ``True`` if every model unlocked successfully, ``False`` otherwise.
        """
        for model in self._sunspec_models.values():
            if not model.unlock():
                return False
            
        self._locked = False
        return True
    
    @property
    def is_locked(self) -> bool:
        """Return whether device models are currently locked."""
        return self._locked
