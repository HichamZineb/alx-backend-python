#!/usr/bin/env python3
"""
Module with a type-annotated function floor that
takes a float as an argument and returns its floor.
"""

import math


def floor(n: float) -> int:
    """
    Function that returns the floor of a given float.

    Args:
        n (float): The input float.

    Returns:
        int: The floor of the input float.
    """
    return math.floor(n)
