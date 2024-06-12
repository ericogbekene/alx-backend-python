#!/usr/bin/env python3
"""
importing a module to generate async comprehension
"""


import asyncio
from typing import Generator, Iterable, List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    generating an async comprehension
    """
    results: List[float] = [item async for item in async_generator()]
    return results
