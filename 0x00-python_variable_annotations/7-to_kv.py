#!/usr/bin/env python3
"""
module to return a tuple
"""
from typing import Tuple, Union

def to_kv(k: str, v: Union[int, float]) -> Tuple[float]:
    """
    function to return a custom tuple
    """
    return tuple((k, float(v ** 2)))
