async-sunspec
=============

.. image:: https://github.com/fundacaocerti/async-sunspec/actions/workflows/ci.yml/badge.svg?branch=master
   :target: https://github.com/fundacaocerti/async-sunspec/actions/workflows/ci.yml

``async-sunspec`` is an asynchronous Modbus communication library for Python 
focused on SunSpec-compliant devices. It provides tools to create both SunSpec 
clients and servers, with a runtime model system for representing SunSpec data 
structures and a modular architecture.

It is an async-first library built on top of `pymodbus`, meant to handle 
multiple devices concurrently without blocking. The client supports scanning for 
SunSpec devices and reading their models asynchronously.

Features
--------

Usage overview
--------------

Configure a server (device): assemble model instances, bind them to a
``SunSpecDevice`` and run the Modbus server.

Configure a client (master): create a ``SunSpecClient``, connect to a device, 
scan for models and interact with them asynchronously.

Advantages
----------

- Scalable concurrency: asyncio-based I/O lets a single process manage many
    connections efficiently.

Requirements
------------

- Python ``>=3.12``
- ``pymodbus==3.12.1``

License
-------

Release under the Mozilla Public License Version 2.0. 
See ``LICENSE.md`` for details.