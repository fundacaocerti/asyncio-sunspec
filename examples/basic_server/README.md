# Basic Server Example

This example runs a SunSpec TCP server with:

- `Model1` (common identity model)
- `Model701` (DER AC measurements)

`Model701` values are updated every few seconds so clients can observe changing telemetry.

## Example Structure

- `device.py`: shows how to build a `SunSpecServerDevice` and populate models.
- `server.py`: shows how to run the server and simulation tasks together.
- `run.py`: CLI entrypoint for local execution.

This split is intentional so users can copy the parts they need into their own projects.

## Run

From the repository root:

```bash
.venv/bin/python examples/basic_server/run.py
```

With custom options:

```bash
.venv/bin/python examples/basic_server/run.py \
  --host 127.0.0.1 \
  --port 15020 \
  --device-id 1 \
  --address 40000 \
  --update-interval 1.0
```

## Read From A Client

In another terminal, you can use the project client example:

```bash
.venv/bin/python client.py
```

The server prints the simulated state transitions (`OFF`/`ON`) and power/current values as they change.

If `5020` is already in use, choose a different port with `--port`.

## Programmatic Consumption

You can consume these helpers directly:

```python
import asyncio

from examples.basic_server.device import build_example_device
from examples.basic_server.server import run_sunspec_server


async def main():
    device, _ = build_example_device(device_id=1, address=40000)
    await run_sunspec_server(host="127.0.0.1", port=15020, device=device)


if __name__ == "__main__":
    asyncio.run(main())
```
