#!/usr/bin/env python3
"""
module to measure parallel runtime
"""


import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    async coroutine to measure runtime
    """
    start_time: float = asyncio.get_event_loop().time()
    await asyncio.gather\
        (async_comprehension(), async_comprehension(),
         async_comprehension(), async_comprehension())
    end_time: float = asyncio.get_event_loop().time()
    total_time: float = end_time - start_time
    return total_time
