#!/usr/bin/env python3
"""
Module with type-annotated function safely_get_value that
retrieves a value from a dictionary safely with a default value.
"""

from typing import Mapping, Any, TypeVar, Union, Optional

T = TypeVar('T')


def safely_get_value(
    dct: Mapping,
    key: Any,
    default: Optional[T] = None
) -> Union[Any, T]:
    """
    Function that retrieves a value
    from a dictionary safely with a default value.

    Args:
        dct (Mapping): The input dictionary.
        key (Any): The key to retrieve from the dictionary.
        default (Optional[T]): The default value if the key is not found.

    Returns:
        Union[Any, T]: The value associated with the key
        or the default value if not found.
    """
    if key in dct:
        return dct[key]
    else:
        return default
