import pytest

from async_sunspec.device import SUNSPEC_END_MODEL, SUNSPEC_HEADER, SunSpecDevice
from async_sunspec.model import SunSpecModel
from async_sunspec.models.model_1 import Model1
from tests.unit.async_sunspec._fixtures import FooModel


def test_model_registry_returns_imported_model_classes() -> None:
    """Expose imported model classes through the global model registry."""
    assert Model1 is SunSpecModel.get_model_class(1)
    assert FooModel is SunSpecModel.get_model_class(0x0420)


def test_repeating_blocks_update_counter_and_model_length() -> None:
    """Update repeating-block counters and total model length correctly."""
    model = FooModel()

    first = model.grp.create_element()
    first.f1 = 1
    first.f2 = "A"
    model.grp.add_element(first)

    second = model.grp.create_element()
    second.f1 = 2
    second.f2 = "B"
    model.grp.add_element(second)

    assert 2 == model.cnt
    assert 34 == model.process_elements()


def test_device_bind_register_populates_header_and_end_marker() -> None:
    """Write SunSpec header/end markers and model offsets on bind."""
    device = SunSpecDevice(device_id=7, address=40_000)
    model = Model1()
    device.add_model(model)

    device.bind_register()

    assert SUNSPEC_HEADER == tuple(device._register[:2])
    assert SUNSPEC_END_MODEL == tuple(device._register[-2:])
    assert 2 == model.offset


def test_device_lock_and_unlock_updates_state_and_model_length() -> None:
    """Set lock state and maintain model L field semantics."""
    device = SunSpecDevice(device_id=7, address=40_000)
    model = FooModel()
    device.add_model(model)
    device.bind_register()

    assert device.lock() is True
    assert device.is_locked is True
    assert model.length - 2 == model.L

    assert device.unlock() is True
    assert device.is_locked is False
    assert 0 == model.L


def test_device_rejects_duplicate_model_ids() -> None:
    """Disallow adding two models with the same model id."""
    device = SunSpecDevice()
    device.add_model(Model1())

    with pytest.raises(ValueError):
        device.add_model(Model1())


def test_device_remove_model_deletes_existing_model() -> None:
    """Remove existing models by id."""
    device = SunSpecDevice()
    model = Model1()
    device.add_model(model)

    device.remove_model(model.id)

    assert device._sunspec_models == {}


def test_device_remove_model_rejects_unknown_model_id() -> None:
    """Raise when removing a model id that is not in the device."""
    device = SunSpecDevice()

    with pytest.raises(ValueError):
        device.remove_model(9999)
