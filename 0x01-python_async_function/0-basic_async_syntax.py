#!/usr/bin/env python3
"""Function that uses basics of async."""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Use asyncio to show concurrency."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
