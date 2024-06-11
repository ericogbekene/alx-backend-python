#!/usr/bin/env python3
"""
running multiple concurrencies
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    async routing to run wait_random multiple times
    """
    # await asyncio.gather(wait_random(max_delay) * n)
    results = [await wait_random(max_delay) for _ in range(n)]

    for i in range(len(results)):
        for j in range(len(results) - i - 1):
            if results[j] > results[j + 1]:
                results[j], results[j + 1] = results[j + 1], results[j]
    return results
