#!/usr/bin/env python3
"""
Module documentation - 2-measure_runtime

This module contains a coroutine 'measure_runtime' that executes
'async_comprehension' four times in parallel using asyncio.gather
and measures the total runtime.

"""

import asyncio
from time import perf_counter

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that executes 'async_comprehension' four times in parallel
    using asyncio.gather and measures the total runtime.

    Returns:
        float: Total runtime.

    """
    start_time = perf_counter()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = perf_counter()
    return end_time - start_time
