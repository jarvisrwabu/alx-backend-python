#!/usr/bin/env python3
"""Function that executes multiple coroutines."""
from typing import List
basic_async = __import__('0-basic_async_syntax')


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Use multiple coroutines."""
    delays = []
    for _ in range(n):
        delay = await basic_async.wait_random(max_delay)
        delays.append(delay)

    return sorted(delays)
