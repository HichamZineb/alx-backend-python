#!/usr/bin/env python3
"""
Module with a type-annotated function to_kv that
takes a string and an int or float and returns a tuple.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Function that returns a tuple with the string
    and the square of the int/float.

    Args:
        k (str): The input string.
        v (Union[int, float]): The input int or float.

    Returns:
        Tuple[str, float]: A tuple containing the string
        and the square of the int/float.
    """
    return (k, v ** 2.0)
