#!/usr/bin/env python3
"""Function that returns sum of floating point nums in list."""
from typing import List


def sum_list(a: List[float]) -> float:
    """Return sum of all the floating point numbers."""
    s: float = 0.0
    for num in a:
        s += num
    return s
