#!/usr/bin/env python3
"""
creating async io task
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    create and return an async io task
    """
    my_task = asyncio.create_task(wait_random(max_delay))
    return my_task
