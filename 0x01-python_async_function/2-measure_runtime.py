#!/usr/bin/env python3
"""
Module documentation - 2-measure_runtime

This module contains a function 'measure_time' that measures
the total execution time for 'wait_n' coroutine and returns
total_time / n.

"""

from typing import List
import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for 'wait_n' coroutine.

    Args:
        n (int): Number of times to spawn 'wait_random'.
        max_delay (int): Maximum delay for each 'wait_random' coroutine.

    Returns:
        float: Total execution time / n.

    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    total_time = end_time - start_time
    return total_time / n
