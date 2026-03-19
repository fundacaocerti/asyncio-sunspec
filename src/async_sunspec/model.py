# *****************************************************************************
# Copyright (c) 2026 CERTI Foundation.
#
# This Source Code Form is subject to the terms of the Mozilla Public 
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# *****************************************************************************
"""Define SunSpec model base behavior and runtime model registry."""

from __future__ import annotations

from typing import Annotated

from .group import SunSpecGroup

_MODEL_REGISTRY: dict[int, type[SunSpecModel]] = {}


class SunSpecModel(SunSpecGroup):
    """Represent a SunSpec model with mandatory ``ID`` and ``L`` points."""

    ID: Annotated[int, ("SunSpecPoint", {"name": "ID", "ptype": "uint16", "value": 0, "mandatory": True, "static": True})]
    L: Annotated[int, ("SunSpecPoint", {"name": "L", "ptype": "uint16", "value": 0, "mandatory": True, "static": True})]

    def __init_subclass__(cls, *, model_name: str, id: int, **kwargs) -> None:
        """Register subclasses by model ID when they are imported.

        Called automatically by Python when a class inherits from
        :class:`SunSpecModel`.  Stores the class in the module-level
        ``_MODEL_REGISTRY`` keyed by ``id``.

        Args:
            model_name: Human-readable model label (e.g. ``"Common"``).
            id: Numeric SunSpec model identifier.  Note: this parameter
                shadows the Python built-in ``id``; use ``model_id`` in
                application code to avoid confusion.
            **kwargs: Forwarded to :meth:`super().__init_subclass__`.
        """
        super().__init_subclass__(**kwargs)
        cls._model_name = model_name
        cls._id = id
        _MODEL_REGISTRY[id] = cls

    @classmethod
    def get_model_class(cls, model_id: int) -> type[SunSpecModel] | None:
        """Return the registered model class for ``model_id`` if available.

        Args:
            model_id: Numeric SunSpec model identifier.

        Returns:
            The :class:`SunSpecModel` subclass registered under
            ``model_id``, or ``None`` if no matching model has been
            imported.
        """
        return _MODEL_REGISTRY.get(model_id)

    @property
    def model_name(self) -> str:
        """Return human-readable model name metadata."""
        return self._model_name

    @property
    def id(self) -> int:
        """Return numeric SunSpec model ID."""
        return self._id
    
    @property
    def offset(self) -> int:
        """Return model offset within its parent device register map."""
        return self._offset
    
    @offset.setter
    def offset(self, offset: int) -> None:
        """Set model offset within its parent device register map."""
        self._offset = offset
    
    def lock(self) -> bool:
        """Lock child elements and freeze ``L`` to current model payload length.

        Calls :meth:`process_elements` to recompute sizes, locks every child
        element, then writes the payload length (``self._length - 2``) into
        the ``L`` point so it is stable for server reads.

        Returns:
            ``True`` if all children locked successfully, ``False`` otherwise.
        """
        self.process_elements()

        for element in self._sunspec_elements.values():
            if not element.lock():
                return False

        L = self._sunspec_elements["L"]
        L.unlock()
        L.value = self._length - 2
        L.lock()

        return True

    def unlock(self) -> bool:
        """Unlock child elements and reset ``L`` to zero.

        Returns:
            ``True`` if all children unlocked successfully, ``False`` otherwise.
        """
        for element in self._sunspec_elements.values():
            if not element.unlock():
                return False

        L = self._sunspec_elements["L"]
        L.value = 0
        return True
