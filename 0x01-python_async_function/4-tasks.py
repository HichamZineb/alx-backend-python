#!/usr/bin/env python3
"""
Module documentation - 4-tasks

This module contains a function 'task_wait_n' that takes two
integer arguments 'n' and 'max_delay'. It spawns 'task_wait_random'
coroutine 'n' times with the specified 'max_delay'.

"""

from typing import List
import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that spawns 'task_wait_random' coroutine 'n' times.

    Args:
        n (int): Number of times to spawn 'task_wait_random'.
        max_delay (int): Maximum delay for each 'task_wait_random' coroutine.

    Returns:
        List[float]: List of delays in ascending order.

    """
    delays = []
    tasks = []

    for _ in range(n):
        tasks.append(task_wait_random(max_delay))

    for task in asyncio.as_completed(tasks):
        delays.append(await task)

    return delays
