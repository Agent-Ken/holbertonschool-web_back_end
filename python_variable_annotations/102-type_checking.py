#!/usr/bin/env python3
"""A simple Python module with type annotations."""

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Zoom in on an array by duplicating its elements."""
    zoomed_in: List = [
        item for item in lst
        for _ in range(factor)
         ]
    return zoomed_in


array: Tuple[int, int, int] = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
