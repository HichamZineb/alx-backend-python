#!/usr/bin/env python3
"""
Module with a duck-typed function safe_first_element that
returns the first element of a sequence or None if the sequence is empty.
"""

from typing import Sequence, Any, Union, Optional


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Function that returns the first element of a sequence
    or None if the sequence is empty.

    Args:
        lst (Sequence[Any]): The input sequence.

    Returns:
        Union[Any, None]: The first element of the sequence or
        None if the sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
