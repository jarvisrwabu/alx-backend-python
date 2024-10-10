#!/usr/bin/env python3
"""Function that returns sum of mixed items in list."""
from typing import List, Union


def sum_mixed_list(a: List[Union[int, float]]) -> float:
    """Return sum of all the numbers."""
    s: float = 0.0
    for num in a:
        s += num
    return s
