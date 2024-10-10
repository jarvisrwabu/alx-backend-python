#!/usr/bin/env python3
"""Returns a function that multiplies a float by multiplier."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by the given multiplier."""
    def multiply(x: float) -> float:
        """Return the product of x and the multiplier."""
        return x * multiplier
    return multiply
