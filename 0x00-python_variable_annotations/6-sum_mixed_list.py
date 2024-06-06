#!/usr/bin/env python3
"""
module to compute sum of a List
with mixed values
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    returning the Sum of a mixed list
    """
    return sum(mxd_lst)
