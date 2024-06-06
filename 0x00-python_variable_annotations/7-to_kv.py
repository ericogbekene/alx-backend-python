#!/usr/bin/env python3
"""
module to return a tuple
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    function to return a custom tuple
    """
    try:
        return tuple((k, float(v) ** 2))
    except ValueError:
        raise TypeError("Value must be convertible to float.")
