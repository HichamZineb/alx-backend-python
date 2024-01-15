#!/usr/bin/env python3
"""
Module documentation - 3-tasks

This module contains a function 'task_wait_random' that
takes an integer 'max_delay' and returns an asyncio.Task.

"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio.Task for the wait_random coroutine.

    Args:
        max_delay (int): Maximum delay for wait_random coroutine.

    Returns:
        asyncio.Task: Task object for the wait_random coroutine.

    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
