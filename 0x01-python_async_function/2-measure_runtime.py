#!/usr/bin/env python3
"""
module to measure runtime
"""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    function to measure average runtime
    """
    starting_time = time.perf_counter()
    await wait_n(n, max_delay)
    total_time = time.perf_counter() - starting_time
    return float(total_time/n)
