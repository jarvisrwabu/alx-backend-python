#!/usr/bin/env python3
"""Function that returns tuple of inputs."""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return tuple of inputs."""
    return (k, v**2)
