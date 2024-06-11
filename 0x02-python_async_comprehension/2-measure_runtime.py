#!/usr/bin/env python3
"""
module to measure parallel runtime
"""


import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """
    async coroutine to measure runtime
    """
    start_time = asyncio.get_event_loop().time()
    await asyncio.gather\
        (async_comprehension(), async_comprehension(),
         async_comprehension(), async_comprehension())
    end_time = asyncio.get_event_loop().time()
    total_time = end_time - start_time
    print(f"Total runtime: {total_time:.2f} seconds")
    return total_time
