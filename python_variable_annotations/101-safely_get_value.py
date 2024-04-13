#!/usr/bin/env python3
"""A simple Python module with type annotations."""

from typing import Mapping, TypeVar, Any
T = TypeVar('T')


def safely_get_value(dct: Mapping[Any, T], key: Any, default: T = None) -> T:
    """Retrieve the value for a given key from a dictionary safely.
    Returns:
        The value associated with the key if it exists, otherwise the default.
    """
    if key in dct:
        return dct[key]
    else:
        return default
