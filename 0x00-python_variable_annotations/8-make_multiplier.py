#!/usr/bin/env python3
"""
module to return a callable function
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    function that returns a Callable
    """
    def multiplier_function(x: float) -> float:
        """
        inner multiplier function
        """
        return x * multiplier
    return multiplier_function
