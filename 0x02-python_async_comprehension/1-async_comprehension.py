#!/usr/bin/env python3
"""
Module documentation - 1-async_comprehension

This module contains a coroutine 'async_comprehension' that
collects 10 random numbers using an async comprehension over
'async_generator'.

"""

import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using an async comprehension.

    Returns:
        List[float]: List of 10 random numbers.

    """
    return [i async for i in async_generator()]
