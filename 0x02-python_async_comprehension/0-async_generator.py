#!/usr/bin/env python3
"""
Module documentation - 0-async_generator

This module contains a coroutine 'async_generator' that loops
10 times, asynchronously waits 1 second, then yields a random
number between 0 and 10 using the random module.

"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Coroutine that yields a random number between 0 and 10.

    Yields:
        float: Random number between 0 and 10.

    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
