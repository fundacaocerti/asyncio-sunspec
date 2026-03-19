from array import array

import pytest
from pymodbus.constants import ExcCodes
from pymodbus.datastore import ModbusDeviceContext

from async_sunspec.models.model_1 import Model1
from async_sunspec.server.device import SunSpecArrayDataBlock, SunSpecServerDevice


def test_constructor_rejects_non_array_values() -> None:
    """Require array-backed storage for SunSpec server data blocks."""
    with pytest.raises(ValueError):
        SunSpecArrayDataBlock(0, [1, 2, 3])


def test_get_and_set_values_use_the_address_offset() -> None:
    """Read/write values using datastore-relative offsets."""
    block = SunSpecArrayDataBlock(10, array("H", [1, 2, 3]))

    assert [1, 2] == list(block.getValues(10, 2))
    assert block.setValues(11, [8, 9]) is None
    assert [1, 8, 9] == list(block.getValues(10, 3))


def test_illegal_addresses_return_modbus_error_code() -> None:
    """Return Modbus illegal-address codes for out-of-range access."""
    block = SunSpecArrayDataBlock(10, array("H", [1, 2, 3]))

    assert ExcCodes.ILLEGAL_ADDRESS == block.getValues(9, 1)
    assert ExcCodes.ILLEGAL_ADDRESS == block.setValues(13, [4])


def test_set_values_accepts_single_scalar_value() -> None:
    """Allow scalar writes by internally normalizing them to a list."""
    block = SunSpecArrayDataBlock(10, array("H", [1, 2, 3]))

    assert block.setValues(11, 99) is None
    assert [1, 99, 3] == list(block.getValues(10, 3))


def test_default_reinitializes_store_and_base_address() -> None:
    """Reset datastore values and base address through `default`."""
    block = SunSpecArrayDataBlock(10, array("H", [1, 2, 3]))

    block.default(count=4, value=7)

    assert 0 == block.address
    assert [7, 7, 7, 7] == list(block.getValues(0, 4))


def test_reset_restores_values_to_default_value() -> None:
    """Restore all datastore entries to the configured default value."""
    block = SunSpecArrayDataBlock(10, array("H", [1, 2, 3]))
    block.default(count=4, value=5)
    block.setValues(1, [9, 9])

    block.reset()

    assert [5, 5, 5, 5] == list(block.getValues(0, 4))


def test_get_context_requires_locked_device() -> None:
    """Refuse context creation until device models are locked."""
    device = SunSpecServerDevice(device_id=1, address=40_000)
    device.add_model(Model1())
    device.bind_register()

    with pytest.raises(ValueError):
        device.get_context()


def test_get_context_requires_at_least_one_model() -> None:
    """Refuse context creation when no model has been added."""
    device = SunSpecServerDevice(device_id=1, address=40_000)
    device.lock()

    with pytest.raises(ValueError):
        device.get_context()


def test_get_context_returns_modbus_context_when_ready() -> None:
    """Return a ModbusDeviceContext for a locked, populated device."""
    device = SunSpecServerDevice(device_id=1, address=40_000)
    device.add_model(Model1())
    device.bind_register()
    device.lock()

    context = device.get_context()

    assert isinstance(context, ModbusDeviceContext)
