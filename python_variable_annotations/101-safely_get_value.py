#!/usr/bin/env python3
"""Program to retreat a value from a dictionary."""

from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping[Any, T], key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """Retreat a value from a dictionary.

    If the key is in the dictionary, return its value.
    Otherwise, return the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
