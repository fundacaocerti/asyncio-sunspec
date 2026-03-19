# *****************************************************************************
# Copyright (c) 2026 CERTI Foundation.
#
# This Source Code Form is subject to the terms of the Mozilla Public 
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# *****************************************************************************
"""CLI entrypoint for the basic SunSpec server example."""

import argparse
import asyncio
import logging

from server import run_basic_server_stack


logger = logging.getLogger(__name__)


async def async_main(args: argparse.Namespace) -> None:
    """Run server and simulation with the provided CLI arguments."""
    await run_basic_server_stack(
        host=args.host,
        port=args.port,
        device_id=args.device_id,
        address=args.address,
        update_interval=args.update_interval,
    )


def parse_args() -> argparse.Namespace:
    """Parse CLI options for the example server runtime."""
    parser = argparse.ArgumentParser(
        description="Run a SunSpec TCP server example with live Model 701 values.",
    )
    parser.add_argument("--host", default="127.0.0.1", help="Bind host")
    parser.add_argument("--port", type=int, default=5020, help="Bind TCP port")
    parser.add_argument(
        "--device-id",
        type=int,
        default=1,
        help="Modbus device id used by clients",
    )
    parser.add_argument(
        "--address",
        type=int,
        default=40000,
        help="SunSpec base register address",
    )
    parser.add_argument(
        "--update-interval",
        type=float,
        default=1.0,
        help="Seconds between simulated telemetry updates",
    )
    return parser.parse_args()


def main() -> None:
    """CLI main function."""
    args = parse_args()
    
    # Configure basic logging for the example. Use DEBUG when --verbose is set,
    # otherwise default to INFO so informational messages are visible.
    level = logging.DEBUG
    logging.basicConfig(
        level=level,
        format="[%(asctime)s] %(levelname)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    try:
        asyncio.run(async_main(args))
    except RuntimeError as exc:
        logger.error("[server] Failed to start: %s", exc)
    except KeyboardInterrupt:
        logger.info("[server] Stopped.")


if __name__ == "__main__":
    main()
