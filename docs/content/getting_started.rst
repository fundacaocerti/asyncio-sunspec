Getting Started
===============

Installation
------------

Install the package from PyPI:

.. code-block:: bash

    pip install async-sunspec

Quickstart
----------

It is possible to implement both SunSpec clients and servers with this library. 
The client side is the most common use case, so we'll start with a quick example 
of how to use the client to connect to a SunSpec device and read some data.

Client
******

The use of `async-sunspec` typically involves creating a `SunSpecClient`, 
connecting to a SunSpec device, and interacting with its models. Here's a simple
example:

.. code-block:: python

   import asyncio
   from async_sunspec.client.device import SunSpecClient

   async def main():
       client = SunSpecClient("127.0.0.1", port=15020)
       await client.connect()
       try:
           device = await client.scan(device_id=1, address=40000)
           print(f"Found {len(device._sunspec_models)} model(s)")
       finally:
           client.close()

   asyncio.run(main())

Server
******

It is also possible to configure a device to act as a SunSpec server. This is 
specially useful for testing or simulating devices. It may not be suitable for
production use due to performance and security considerations.

Here is a minimal programmatic example that creates a simple server exposing
one device with a common Model 1 block and a small telemetry model. Save this
as ``simple_server.py`` and run it from the repository root.

.. code-block:: python

   import asyncio
   from async_sunspec.server.server import SunSpecServer
   from async_sunspec.server.device import SunSpecServerDevice
   from async_sunspec.models.model_1 import Model1
   from async_sunspec.models.model_701 import Model701, Model701St

   async def main():
       device = SunSpecServerDevice(device_id=1, address=40000)

       common = Model1(
           Mn="Manufacturer",
           Md="Test Device",
           Opt="basic",
           Vr="1.0.0",
           SN="EXAMPLE-0001",
       )
       device.add_model(common)

       measurements = Model701(LNV=220, LLV=380, Hz=60, W=0, A=0, St=Model701St.OFF)
       device.add_model(measurements)

       server = SunSpecServer(host="127.0.0.1", port=5020, devices=device)
       await server.run()

   if __name__ == "__main__":
       asyncio.run(main())
