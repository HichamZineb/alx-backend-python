#!/usr/bin/env python3
"""
Module with a type-annotated function concat that
concatenates two strings and returns the result.
"""


def concat(str1: str, str2: str) -> str:
    """
    Function that concatenates two strings.

    Args:
        str1 (str): The first string.
        str2 (str): The second string.

    Returns:
        str: The concatenated string.
    """
    return str1 + str2
