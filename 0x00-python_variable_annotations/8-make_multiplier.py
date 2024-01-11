#!/usr/bin/env python3
"""
Module with a type-annotated function make_multiplier that
takes a float multiplier and returns a function.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Function that returns a function to multiply a float by a given multiplier.

    Args:
        multiplier (float): The multiplier value.

    Returns:
        Callable[[float], float]: Function that multiplies float by multiplier.
    """
    def multiplier_function(x: float) -> float:
        """
        Inner function that multiplies a float by the multiplier.

        Args:
            x (float): The input float.

        Returns:
            float: The result of multiplying x by the multiplier.
        """
        return x * multiplier

    return multiplier_function
