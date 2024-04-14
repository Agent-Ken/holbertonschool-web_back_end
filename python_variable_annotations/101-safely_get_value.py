#!/usr/bin/env python3
"""
Module for safely retrieving values from a dictionary.
"""

from typing import Any, Mapping, TypeVar, Union
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Retrieve value for a given key from a dict or return default.
    """
    if key in dct:
        return dct[key]
    else:
        return default
