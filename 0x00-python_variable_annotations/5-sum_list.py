#!/usr/bin/env python3
"""Function that returns sum of floating point nums in list."""


def sum_list(a: list[float]) -> float:
    """Return sum of all the floating point numbers."""
    s: float = 0.0
    for num in a:
        s += num
    return s
