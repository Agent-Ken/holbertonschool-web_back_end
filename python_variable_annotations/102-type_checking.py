#!/usr/bin/env python3
"""A simple Python module with type annotations."""

from typing import Tuple, List, Any


def zoom_array(lst: Tuple[Any, ...], factor: int = 2) -> List[Any]:
    """Zoom in on an array by duplicating its elements.
    Returns:
        A list with the elements of the tuple duplicated 'factor' times.
    """
    zoomed_in: List[Any] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array: Tuple[int, int, int] = (12, 72, 91)

zoom_2x = zoom_array(array)

# changed to int from float to fix the error
zoom_3x = zoom_array(array, 3)
