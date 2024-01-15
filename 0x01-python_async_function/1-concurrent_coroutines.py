#!/usr/bin/env python3
"""
Module documentation - 1-concurrent_coroutines

This module contains an asynchronous coroutine 'wait_n' that takes
two integer arguments 'n' and 'max_delay'. It spawns 'wait_random'
coroutine 'n' times with the specified 'max_delay'.

"""

from typing import List
import asyncio
from random import uniform

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that spawns 'wait_random' coroutine 'n' times.

    Args:
        n (int): Number of times to spawn 'wait_random'.
        max_delay (int): Maximum delay for each 'wait_random' coroutine.

    Returns:
        List[float]: List of delays in ascending order.

    """
    delays = []
    tasks = []

    for _ in range(n):
        tasks.append(wait_random(max_delay))

    for task in asyncio.as_completed(tasks):
        delays.append(await task)

    return delays
