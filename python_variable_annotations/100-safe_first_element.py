#!/usr/bin/env python3
"""A simple Python module with type annotations."""

from typing import Sequence, Any, Union


# Test test test
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Retrieve the first element of a sequence safely if it exists."""
    if lst:
        return lst[0]
    else:
        return None
