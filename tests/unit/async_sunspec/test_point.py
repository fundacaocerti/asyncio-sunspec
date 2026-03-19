from array import array

import pytest

from async_sunspec.point import SunSpecPoint, SunSpecPointAccess


def test_optional_point_defaults_to_not_implemented_value() -> None:
    """Use the SunSpec not-implemented sentinel for optional points."""
    point = SunSpecPoint("optional", "uint16", mandatory=False)

    assert 0xFFFF == point.value


def test_static_point_cannot_be_modified_while_locked() -> None:
    """Prevent writes to static points once the point is locked."""
    point = SunSpecPoint("status", "uint16", value=1, static=True)
    point.lock()

    with pytest.raises(AttributeError):
        point.value = 2


def test_bind_register_preserves_current_value_and_updates_target() -> None:
    """Bind a point to external storage and keep values synchronized."""
    point = SunSpecPoint("power", "uint16", value=7)
    register = array("H", [0])

    point.bind_register(register)
    point.value = 9

    assert [9] == list(register)
    assert 9 == point.value


def test_static_point_must_be_read_only() -> None:
    """Reject invalid static points with writable access metadata."""
    with pytest.raises(ValueError):
        SunSpecPoint(
            "status",
            "uint16",
            static=True,
            access=SunSpecPointAccess.RW,
        )


def test_unknown_point_type_raises_value_error() -> None:
    """Fail fast when creating a point with an unknown type id."""
    with pytest.raises(ValueError):
        SunSpecPoint("mystery", "unknown")
