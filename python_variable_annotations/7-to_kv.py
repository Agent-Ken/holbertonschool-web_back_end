#!/usr/bin/env python3
"""Simple operations with type annotations."""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return tuple of str and squared float."""
    return (k, v ** 2)
