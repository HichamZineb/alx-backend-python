#!/usr/bin/env python3
"""
Module with a type-annotated function zoom_array that
takes a tuple and an optional factor, and returns a list.
"""

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Function that takes a tuple and an optional factor,
    and returns a list by zooming in on each element.

    Args:
        lst (Tuple): The input tuple.
        factor (int): The zoom factor (default is 2).

    Returns:
        List: A list obtained by zooming in on each element.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in
