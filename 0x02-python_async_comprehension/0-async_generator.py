#!/usr/bin/env python3
"""
module to create an async function generator
"""

import asyncio
import random


async def async_generator() -> int:
    """
    async generator to yield a random number
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
