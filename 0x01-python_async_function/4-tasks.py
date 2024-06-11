#!/usr/bin/env python3
"""
running multiple concurrencies
"""

import asyncio
from typing import List
# wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    async routing to run wait_random multiple times
    """
    # await asyncio.gather(wait_random(max_delay) * n)
    return [await task_wait_random(max_delay) for _ in range(n)]
