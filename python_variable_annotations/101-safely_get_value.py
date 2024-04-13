#!/usr/bin/env python3
"""A simple Python module with type annotations."""
from typing import Any, Mapping, Union, TypeVar

T = TypeVar('T')
R = Union[Any, T]
D = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: D = None) -> R:
    """
    Retrieve the value for a given key from a dictionary safely.
    Returns:
        The value associated with the key if it exists, otherwise the default.
    """
    if key in dct:
        return dct[key]
    else:
        return default
