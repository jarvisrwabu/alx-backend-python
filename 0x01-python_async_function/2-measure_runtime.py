#!/usr/bin/env python3
"""Function that gets time taken to complete the program."""
import time
conc = __import__("1-concurrent_coroutines")


async def measure_time(n: int, max_delay: int) -> float:
    """Get time taken to complete program."""
    # Save timestamp
    start = time.time()

    await conc.wait_n(n, max_delay)

    # Save timestamp
    end = time.time()

    total_time = end - start  # Time taken to execute the program

    return total_time / n
