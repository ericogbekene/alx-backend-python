#!/usr/bin/env python3
"""
module to create an async function generator
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> list[float]:
    """
    async generator to yield a random number
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
