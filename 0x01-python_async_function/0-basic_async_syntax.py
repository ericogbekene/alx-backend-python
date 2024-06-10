#!/usr/bin/env python3
"""
function to simulate random delay in async function
"""


import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """
    async coroutine
    """
    sleep_timer = float(random.randint(0, max_delay))
    await asyncio.sleep(sleep_timer)
    return sleep_timer
