#!/usr/bin/env python3
"""Function that executes multiple coroutines."""
basic_async = __import__('0-basic_async_syntax')
from typing import List


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Use multiple coroutines."""
    delays = []
    for _ in range(n):
        delay = await basic_async.wait_random(max_delay)
        delays.append(delay)

    return sorted(delays)
