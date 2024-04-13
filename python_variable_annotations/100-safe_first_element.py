#!/usr/bin/env python3
"""A simple Python module with type annotations."""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Retrieve the first element of a sequence safely.
    Args:
        lst: A sequence of any type.
    Returns:
        The first element of the sequence if it exists, otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None
