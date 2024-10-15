#!/usr/bin/env python3
"""Function that executes multiple coroutines."""
basic_async = __import__('0-basic_async_syntax')


async def wait_n(n: int, max_delay: int) -> list[float]:
    """Use multiple coroutines."""
    delays = []
    for _ in range(n):
        delay = await basic_async.wait_random(max_delay)
        delays.append(delay)

    # Ensure delays are in ascending order as they are completed
    sorted_delays = []
    while delays:
        min_delay = min(delays)
        sorted_delays.append(min_delay)
        delays.remove(min_delay)

    return sorted_delays
