#!/usr/bin/env python3
"""Function that executes multiple coroutines."""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Use multiple coroutines."""
    # Create a list of asyncio.Task objects
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    # Gather the results as they complete
    delays = await asyncio.gather(*tasks)

    # Return the list of delays sorted in ascending order
    return sorted(delays)
