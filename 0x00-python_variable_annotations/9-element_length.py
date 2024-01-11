#!/usr/bin/env python3
"""
Module with a type-annotated function element_length that
takes an iterable and returns a list of tuples with elements
and their lengths.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Function that takes an iterable and returns a list of tuples
    with elements and their lengths.

    Args:
        lst (Iterable[Sequence]): The input iterable.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples with elements
        and their lengths.
    """
    return [(i, len(i)) for i in lst]
