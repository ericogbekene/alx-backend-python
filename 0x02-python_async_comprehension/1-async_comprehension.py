#!/usr/bin/env python3
"""
importing a module to generate async comprehension
"""


import asyncio
from typing import Generator
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Generator[int, None, None]:
    """
    generating an async comprehension
    """
    results = []
    async for item in async_generator():
        results.append(item)
    return results