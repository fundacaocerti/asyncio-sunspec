from array import array

import pytest

from async_sunspec.types import INT32, STRING, UINT16


def test_uint16_round_trip_preserves_value() -> None:
    """Encode/decode uint16 values without losing information."""
    register = array("H", [0])

    UINT16.into_register(42, register)

    assert [42] == list(register)
    assert 42 == UINT16.from_register(register)


def test_uint16_rejects_out_of_range_values() -> None:
    """Reject uint16 values above the protocol limit."""
    register = array("H", [0])

    with pytest.raises(ValueError):
        UINT16.into_register(2**16, register)


def test_int32_round_trip_preserves_negative_value() -> None:
    """Encode/decode signed int32 values, including negatives."""
    register = array("H", [0, 0])

    INT32.into_register(-12_345, register)

    assert -12_345 == INT32.from_register(register)


def test_string_round_trip_preserves_text() -> None:
    """Store short strings and keep trailing register padding zeroed."""
    register = array("H", [0, 0, 0, 0])

    STRING.into_register("AB", register)

    assert "AB" == STRING.from_register(register)
    assert 0 == register[2]
    assert 0 == register[3]


def test_string_rejects_values_that_do_not_fit() -> None:
    """Raise when a string exceeds the allocated register space."""
    register = array("H", [0, 0])

    with pytest.raises(ValueError):
        STRING.into_register("TOO", register)
