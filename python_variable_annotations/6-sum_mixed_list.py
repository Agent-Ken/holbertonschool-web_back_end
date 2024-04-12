#!/usr/bin/env python3
"""Simple operations with type annotations."""

from typing import List, Union


def sum_mixed_list(sum_mixed_list: List[Union[int, float]]) -> float:
    """Return the sum of ints and floats as a float."""
    return sum(sum_mixed_list)
