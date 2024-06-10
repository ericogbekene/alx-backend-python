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
    starting_time = time.strftime("%S")
    await wait_n(n, max_delay)
    elapsed_time = time.strftime("%S")

    total_time = int(elapsed_time) - int(starting_time)
    print(f'total time {total_time}')
    return float(total_time/n)
