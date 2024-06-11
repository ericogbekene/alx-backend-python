#!/usr/bin/env python3
"""
importing a module to generate async comprehension
"""


import asyncio
from typing import Generator, Iterable
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> list[float]:
    """
    generating an async comprehension
    """
    results: list[int]  = []
    async for item in async_generator():
        results.append(item)
    return results
