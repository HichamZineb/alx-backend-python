#!/usr/bin/env python3
"""
Module with a type-annotated function sum_mixed_list that
takes a list of integers and floats as an argument and returns their sum.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Function that returns the sum of a given list of integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): Input list of integers and floats.

    Returns:
        float: The sum of the input list.
    """
    return sum(mxd_lst)
