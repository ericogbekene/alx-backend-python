#!/usr/bin/env python3
"""
module to annotate an iterable returning ductype
"""

from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ annotated function"""
    return [(i, len(i)) for i in lst]