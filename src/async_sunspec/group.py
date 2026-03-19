# *****************************************************************************
# Copyright (c) 2026 CERTI Foundation.
#
# This Source Code Form is subject to the terms of the Mozilla Public 
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# *****************************************************************************
"""Build SunSpec groups dynamically from ``typing.Annotated`` metadata."""

from __future__ import annotations

from array import array
from typing import Any, dataclass_transform, get_type_hints

from .point import SunSpecPoint


@dataclass_transform(field_specifiers=(SunSpecPoint,))
class SunSpecGroupMeta(type):
    """Create group classes with runtime SunSpec element wiring."""

    def __new__(mcs, name, bases, namespace, **kwargs):
        """Construct class attributes and inject a dynamic initializer."""
        # Collect all SunSpecPoint descriptors from base classes and this class
        points = {}

        # Traverse base classes in MRO (excluding 'object')
        for base in reversed(bases):
            hints = get_type_hints(base, include_extras=True)
            for point_name, point_type in hints.items():
                metadata = SunSpecGroupMeta.extract_sunspec_metadata(point_type) 
                if metadata is not None:
                    points[point_name] = metadata

        # Now process the current class's annotations
        for point_name, point_type in namespace.get('__annotations__', {}).items():
            metadata = SunSpecGroupMeta.extract_sunspec_metadata(point_type)
            if metadata is not None:
                points[point_name] = metadata

        # Define a dynamic __init__
        def __init__(self, **kwargs):
            """Initialize runtime elements declared on the group class."""
            self._sunspec_elements = {el: None for el in points}
            self._sunspec_parent = None
            self._length = 0
            self._offset = 0
            for point_name, metadata in points.items():
                instance = SunSpecGroupMeta.build_sunspec_element(metadata, self.namespace)
                self._sunspec_elements[point_name] = instance
                setattr(self, point_name, instance)
                if point_name in kwargs:
                    instance.value = kwargs[point_name]

            if "ID" in self._sunspec_elements and hasattr(self, 'id'):
                self._sunspec_elements["ID"].value = self.id

        def __repr__(self):
            """Return a repr containing point names and resolved values."""
            return f"{name}(" + ", ".join(f"{point_name}={getattr(self, point_name)}" for point_name in points) + ")"

        namespace["__init__"] = __init__
        namespace["__repr__"] = __repr__

        return super().__new__(mcs, name, bases, namespace, **kwargs)

    def __setattr__(cls, name, value) -> None:
        """Prevent replacing declared point descriptors on group classes."""
        if name in cls.__dict__ and isinstance(cls.__dict__[name], SunSpecPoint):
            raise AttributeError(f"Cannot overwrite SunSpecPoint '{name}' on class {cls.__name__}")
        super().__setattr__(name, value)

    @staticmethod
    def extract_sunspec_metadata(annotation: str) -> dict[str, Any] | None:
        """Extract the first SunSpec metadata tuple from an annotation.

        Inspects ``__metadata__`` on ``typing.Annotated`` annotations and
        returns the first tuple whose first element starts with ``"SunSpec"``.

        Args:
            annotation: A type annotation, typically from
                :func:`typing.get_type_hints`.

        Returns:
            The matching metadata tuple, or ``None`` if no SunSpec metadata
            is found.
        """
        metadata = ()
        if hasattr(annotation, '__metadata__'):
            metadata = annotation.__metadata__

        for meta in metadata:
            if not isinstance(meta, tuple) or len(meta) == 0:
                continue

            if meta[0].startswith("SunSpec"):
                return meta
            
        return None
    
    @staticmethod
    def build_sunspec_element(metadata: tuple, namespace: dict[str, Any]) -> Any:
        """Instantiate an element object from a metadata tuple.

        Args:
            metadata: A SunSpec metadata tuple whose first element is one of
                ``"SunSpecPoint"``, ``"SunSpecGroup"``, or
                ``"SunSpecRepeatingBlock"``, and whose second element is a
                ``dict`` of constructor keyword arguments.
            namespace: The current group's namespace, used to resolve
                counter-point references for repeating blocks.

        Returns:
            A :class:`.SunSpecPoint`, :class:`SunSpecGroup`, or
            :class:`SunSpecRepeatingBlock` instance.

        Raises:
            ValueError: If the SunSpec element type is not recognised.
        """
        sunspec_type, kwargs = metadata[0], metadata[1]
        match(sunspec_type):
            case "SunSpecPoint":
                return SunSpecPoint.create(namespace, **kwargs)
            case "SunSpecGroup":
                group_type = kwargs.get("group_type", SunSpecGroup)
                return group_type.create(namespace, **kwargs)
            case "SunSpecRepeatingBlock":
                return SunSpecRepeatingBlock.create(namespace, **kwargs)
            case _:
                raise ValueError(f"Unknown SunSpec element type: {sunspec_type}")

class SunSpecGroup(metaclass=SunSpecGroupMeta):
    """Represent a structured SunSpec element composed of points and groups."""

    def __setattr__(self, name, value):
        """Redirect point assignment to point value updates."""
        # Intercept assignments to SunSpecPoint fields
        attr = self.__dict__.get(name)
        if isinstance(attr, SunSpecPoint):
            attr.value = value
            return
        super().__setattr__(name, value)

    def __getattribute__(self, name):
        """Return decoded values when accessing point attributes."""
        # Intercept attribute access for SunSpecPoint fields
        _sunspec_elements = object.__getattribute__(self, "__dict__").get('_sunspec_elements', {})
        if isinstance(_sunspec_elements.get(name), SunSpecPoint):
            point = _sunspec_elements[name]
            return point.value
        return object.__getattribute__(self, name)
    
    @classmethod
    def create(cls, namespace: dict[str, Any], **kwargs) -> SunSpecGroup:
        """Create a group instance from metadata kwargs.

        Args:
            namespace: Parent group namespace (unused directly; passed for
                API symmetry with :class:`SunSpecRepeatingBlock`).
            **kwargs: Keyword arguments forwarded to :meth:`__init__`.

        Returns:
            A new instance of this group class.
        """
        return cls(**kwargs)
    
    @property
    def parent(self) -> SunSpecGroup | None:
        """Return the parent group, when attached."""
        return self._sunspec_parent
    
    @parent.setter
    def parent(self, parent: SunSpecGroup | None) -> None:
        """Set the parent group reference."""
        self._sunspec_parent = parent

    @property
    def namespace(self) -> dict[str, Any]:
        """Return visible elements merged with parent namespace entries."""
        parent_namespace = self.parent.namespace if self.parent is not None else {}
        return {**parent_namespace, **self._sunspec_elements}
    
    @property
    def length(self) -> int:
        """Return serialized group length in registers."""
        return self._length
    
    def process_elements(self) -> int:
        """Compute offsets and total serialized length for child elements.

        Iterates over all child :class:`.SunSpecPoint`,
        :class:`SunSpecGroup`, and :class:`SunSpecRepeatingBlock` instances,
        assigning each a register offset and summing their sizes.

        Returns:
            Total number of 16-bit registers consumed by this group.
        """
        length = 0
        for element in self._sunspec_elements.values():
            element.offset = length
            if isinstance(element, SunSpecPoint):
                length += element.size
            elif isinstance(element, SunSpecGroup):
                element.process_elements()
                length += element.length
            elif isinstance(element, SunSpecRepeatingBlock):
                for block_element in element:
                    block_element.parent = self
                    block_element.offset = length
                    block_element.process_elements()
                    length += block_element.length
        self._length = length
        return length
    
    def bind_register(self, register: array | memoryview) -> None:
        """Bind all elements to slices of the provided register buffer.

        Calls :meth:`process_elements` first, then slices ``register`` for
        each child element using its computed offset and size.

        Args:
            register: A writable ``array`` or ``memoryview`` large enough
                to hold :attr:`length` registers.
        """
        self.process_elements()

        self._register = register

        for el in self._sunspec_elements.values():
            if isinstance(el, SunSpecPoint):
                el.bind_register(memoryview(self._register)[el.offset : el.offset + el.size])
            elif isinstance(el, SunSpecGroup):
                el.bind_register(memoryview(self._register)[el.offset : el.offset + el.length])
            elif isinstance(el, SunSpecRepeatingBlock):
                for block_element in el:
                    block_element.bind_register(memoryview(self._register)[block_element.offset : block_element.offset + block_element.length])
    
    def read_from_register(self, register: array | memoryview) -> None:
        """Bind children to a register buffer and decode dynamic structures.

        Performs two passes when :class:`SunSpecRepeatingBlock` children are
        present: first binds static points so counter values are readable,
        then rebuilds repeating-block element lists from those counters.

        Args:
            register: A ``memoryview`` or ``array`` containing raw register
                data fetched from a remote device.
        """
        self._register = register

        # First pass: bind points so counter values are available
        offset = 0
        for el in self._sunspec_elements.values():
            el.offset = offset
            if isinstance(el, SunSpecPoint):
                el.read_from_register(memoryview(self._register)[offset : offset + el.size])
                offset += el.size
            elif isinstance(el, SunSpecGroup):
                el.read_from_register(memoryview(self._register)[offset : offset + el.length])
                offset += el.length
            elif isinstance(el, SunSpecRepeatingBlock):
                el.read_from_register(memoryview(self._register)[offset:])
                offset += el.length

        self._length = offset

    def lock(self) -> bool:
        """Lock every child element and return success."""
        for element in self._sunspec_elements.values():
            if not element.lock():
                return False
        return True

    def unlock(self) -> bool:
        """Unlock every child element and return success."""
        for point in self._sunspec_elements.values():
            if not point.unlock():
                return False
        return True

class SunSpecRepeatingBlock[T]:
    """Store a runtime-sized sequence of homogeneous SunSpec groups."""
    
    def __init__(self, *, block_type: type[T], counter: SunSpecPoint) -> None:
        """Initialize a repeating block linked to a counter point.

        Args:
            block_type: The concrete :class:`SunSpecGroup` subclass used
                to instantiate each element.
            counter: A :class:`.SunSpecPoint` (typically ``uint16``) whose
                value always reflects the current number of elements.
        """
        self._block_type = block_type
        self._counter = counter
        self._elements: list[T] = []
        self._offset = 0
        self._locked = False

    @classmethod
    def create(cls, namespace: dict[str, Any], **kwargs) -> SunSpecRepeatingBlock:
        """Create a repeating block from metadata kwargs.

        Pops ``group_type`` and ``counter`` from ``kwargs``, resolves the
        counter point from ``namespace``, and constructs the block.

        Args:
            namespace: The parent group's element namespace used to look up
                the counter point by name.
            **kwargs: Must include ``group_type`` (the element class) and
                ``counter`` (the counter point name string).

        Returns:
            A new :class:`SunSpecRepeatingBlock` instance.
        """
        block_type = kwargs.pop("group_type")
        counter_name = kwargs.pop("counter")
        counter = namespace[counter_name]
        return cls(block_type=block_type, counter=counter)

    @property
    def create_element(self) -> type[T]:
        """Return the concrete group type expected by this block."""
        return self._block_type
    
    def add_element(self, element: T) -> None:
        """Append an element and update the backing counter point.

        Args:
            element: An instance of the block's ``block_type``.

        Raises:
            RuntimeError: If the block is locked.
            TypeError: If ``element`` is not an instance of ``block_type``.
        """
        if self._locked:
            raise RuntimeError("Cannot add elements to a locked block")
        if not isinstance(element, self._block_type):
            raise TypeError(f"Expected element of type {self._block_type.__name__}, got {type(element).__name__}")
        self._elements.append(element)
        self._counter.value = len(self._elements)

    def remove_element(self, index: int) -> None:
        """Remove an element by index and update the backing counter point.

        Args:
            index: Zero-based position of the element to remove.

        Raises:
            RuntimeError: If the block is locked.
            IndexError: If ``index`` is out of range.
        """
        if self._locked:
            raise RuntimeError("Cannot remove elements from a locked block")
        del self[index]

    def clear_elements(self) -> None:
        """Remove all elements and reset the backing counter point."""
        if self._locked:
            raise RuntimeError("Cannot clear elements of a locked block")
        self._elements.clear()
        self._counter.value = 0

    def __getitem__(self, key: int) -> T:
        """Return one block element by index."""
        if key < 0 or key >= len(self._elements):
            raise IndexError("Index out of range")
        return self._elements[key]
    
    def __setitem__(self, key: int, value: T) -> None:
        """Replace one block element by index."""
        if self._locked:
            raise RuntimeError("Cannot modify elements of a locked block")
        if key < 0 or key >= len(self._elements):
            raise IndexError("Index out of range")
        if not isinstance(value, self._block_type):
            raise TypeError(f"Expected element of type {self._block_type.__name__}, got {type(value).__name__}")
        self._elements[key] = value

    def __delitem__(self, key: int) -> None:
        """Delete one block element by index and update the counter."""
        if self._locked:
            raise RuntimeError("Cannot delete elements from a locked block")
        if key < 0 or key >= len(self._elements):
            raise IndexError("Index out of range")
        del self._elements[key]
        self._counter.value = len(self._elements)

    def __len__(self):
        """Return current number of elements in this block."""
        return len(self._elements)
    
    def __iter__(self):
        """Iterate over block elements in insertion order."""
        return iter(self._elements)
    
    def __repr__(self):
        """Return a repr containing all block elements."""
        return f"[{', '.join(repr(el) for el in self._elements)}]"
    
    @property
    def offset(self) -> int:
        """Return block offset relative to its parent group."""
        return self._offset
    
    @offset.setter
    def offset(self, offset: int) -> None:
        """Set block offset relative to its parent group."""
        self._offset = offset

    @property
    def counter(self) -> int:
        """Return the current counter-point value."""
        return self._counter.value
    
    @property
    def length(self) -> int:
        """Return total serialized size of all block elements."""
        return sum(el.length for el in self._elements)
    
    def lock(self) -> bool:
        """Lock every element in the block and return success."""
        for element in self._elements:
            if not element.lock():
                return False
        self._locked = True
        return True
    
    def unlock(self) -> bool:
        """Unlock every element in the block and return success."""
        for element in self._elements:
            if not element.unlock():
                return False
        self._locked = False
        return True

    def read_from_register(self, register: memoryview) -> None:
        """Rebuild block elements by decoding values from a register view.

        Reads the counter point value, clears existing elements, then
        reconstructs each element by calling
        :meth:`.SunSpecGroup.read_from_register` on a fresh instance.

        Args:
            register: A :class:`memoryview` starting at this block's offset
                within the parent device register buffer.
        """
        count = self._counter.value
        self._elements.clear()

        offset = 0
        for _ in range(count):
            element = self._block_type()
            element.parent = self
            element.read_from_register(register[offset:])
            element.offset = offset
            self._elements.append(element)
            offset += element.length
