#!/usr/bin/env python3
"""Function that returns sum of floating point nums in list."""


def floor(a: list[float]) -> float:
    """Return sum of all the floating point numbers."""
    sum: float = 0.0
    for num in a:
        sum += num
    return sum
