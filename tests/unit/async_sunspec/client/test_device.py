import asyncio
from array import array

import pytest

from async_sunspec.client.device import SunSpecClient
from async_sunspec.device import SUNSPEC_END_MODEL, SUNSPEC_HEADER, SunSpecDevice
from async_sunspec.models.model_1 import Model1
from tests.unit.async_sunspec._fixtures import FooModel


def _build_model_1_register(**kwargs) -> array:
    """Build a Model1 register payload suitable for client read tests."""
    model = Model1(
        Mn=kwargs.get("Mn", "M"),
        Md=kwargs.get("Md", "D"),
        Opt=kwargs.get("Opt", "O"),
        Vr=kwargs.get("Vr", "V"),
        SN=kwargs.get("SN", "S"),
        DA=kwargs.get("DA", 1),
    )
    register = array("H", [0] * model.process_elements())
    model.bind_register(register)
    model.lock()
    return register


def test_read_registers_returns_response_registers() -> None:
    """Return the Modbus register list when the response is successful."""

    class FakeResponse:
        registers = [1, 2, 3]

        def isError(self) -> bool:
            return False

    class FakeClient:
        async def read_holding_registers(self, address, count, device_id):
            return FakeResponse()

    client = SunSpecClient("127.0.0.1")
    client._client = FakeClient()

    registers = asyncio.run(client._read_registers(address=100, count=3, device_id=1))

    assert [1, 2, 3] == registers


def test_read_registers_raises_on_modbus_error() -> None:
    """Raise when the underlying Modbus response indicates an error."""

    class FakeResponse:
        def isError(self) -> bool:
            return True

    class FakeClient:
        async def read_holding_registers(self, address, count, device_id):
            return FakeResponse()

    client = SunSpecClient("127.0.0.1")
    client._client = FakeClient()

    with pytest.raises(IOError):
        asyncio.run(client._read_registers(address=100, count=3, device_id=1))


def test_scan_raises_when_sunspec_header_is_missing(monkeypatch: pytest.MonkeyPatch) -> None:
    """Fail fast if the SunSpec identification header is not found."""

    async def fake_read(self, address: int, count: int, device_id: int) -> list[int]:
        return [0, 0]

    monkeypatch.setattr(SunSpecClient, "_read_registers", fake_read)
    client = SunSpecClient("127.0.0.1")

    with pytest.raises(ValueError):
        asyncio.run(client.scan(device_id=1, address=40_000))


def test_scan_skips_unknown_models_and_stops_at_end(monkeypatch: pytest.MonkeyPatch) -> None:
    """Skip unknown model ids and finish scan when end marker is reached."""
    base = 40_000
    unknown_model_id = 9999
    unknown_length = 4
    offset = base + 2
    end_offset = offset + 2 + unknown_length

    responses = {
        (base, 2): list(SUNSPEC_HEADER),
        (offset, 2): [unknown_model_id, unknown_length],
        (end_offset, 2): list(SUNSPEC_END_MODEL),
    }

    async def fake_read(self, address: int, count: int, device_id: int) -> list[int]:
        return responses[(address, count)]

    monkeypatch.setattr(SunSpecClient, "_read_registers", fake_read)
    client = SunSpecClient("127.0.0.1")

    device = asyncio.run(client.scan(device_id=1, address=base))

    assert isinstance(device, SunSpecDevice)
    assert {} == device._sunspec_models


def test_scan_reads_known_model_payload(monkeypatch: pytest.MonkeyPatch) -> None:
    """Decode a known model payload and add it to the scanned device."""
    base = 40_000
    offset = base + 2
    model_register = _build_model_1_register(DA=42)
    model_id = model_register[0]
    model_length = model_register[1]
    end_offset = offset + len(model_register)

    responses = {
        (base, 2): list(SUNSPEC_HEADER),
        (offset, 2): [model_id, model_length],
        (offset, len(model_register)): list(model_register),
        (end_offset, 2): list(SUNSPEC_END_MODEL),
    }

    async def fake_read(self, address: int, count: int, device_id: int) -> list[int]:
        return responses[(address, count)]

    monkeypatch.setattr(SunSpecClient, "_read_registers", fake_read)
    client = SunSpecClient("127.0.0.1")

    device = asyncio.run(client.scan(device_id=1, address=base))
    scanned = device._sunspec_models[1]

    assert 1 == scanned.id
    assert 42 == scanned.DA
    assert 2 == scanned.offset


def test_read_model_raises_for_missing_model() -> None:
    """Raise KeyError when trying to read a model that is not present."""
    client = SunSpecClient("127.0.0.1")
    device = SunSpecDevice(device_id=1, address=40_000)

    with pytest.raises(KeyError):
        asyncio.run(client.read_model(device, model_id=1))


def test_read_model_updates_existing_model_from_registers(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Refresh model values from Modbus register data."""
    register = _build_model_1_register(DA=77)
    model = Model1()
    model.lock()
    model.offset = 2

    device = SunSpecDevice(device_id=1, address=40_000)
    device.add_model(model)

    async def fake_read(self, address: int, count: int, device_id: int) -> list[int]:
        return list(register)

    monkeypatch.setattr(SunSpecClient, "_read_registers", fake_read)
    client = SunSpecClient("127.0.0.1")

    result = asyncio.run(client.read_model(device, model_id=1))

    assert result is model
    assert 77 == model.DA


def test_read_all_reads_every_model_in_device(monkeypatch: pytest.MonkeyPatch) -> None:
    """Iterate through every model id and call read_model for each one."""
    device = SunSpecDevice(device_id=1, address=40_000)
    device.add_model(Model1())
    device.add_model(FooModel())
    called: list[int] = []

    async def fake_read_model(self, scan_device: SunSpecDevice, model_id: int):
        called.append(model_id)
        return scan_device._sunspec_models[model_id]

    monkeypatch.setattr(SunSpecClient, "read_model", fake_read_model)
    client = SunSpecClient("127.0.0.1")

    asyncio.run(client.read_all(device))

    assert [1, 0x0420] == called
