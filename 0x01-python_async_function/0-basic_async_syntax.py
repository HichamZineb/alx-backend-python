#!/usr/bin/env python3
"""
Module documentation - 0-basic_async_syntax

This module contains an asynchronous coroutine 'wait_random'
that takes an integer argument 'max_delay' (with a default
value of 10) and waits for a random delay between 0 and max_delay
(inclusive, float value) seconds and eventually returns it.

"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay.

    Args:
        max_delay (int): Maximum delay in seconds (default is 10).

    Returns:
        float: Random delay between 0 and max_delay (inclusive).

    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
