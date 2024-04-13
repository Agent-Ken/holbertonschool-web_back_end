#!/usr/bin/env python3
"""A simple Python module with type annotations."""

from typing import Sequence, Any, Union


def safe_first_element(lst: Union[Sequence[Any], None]) -> Union[Any, None]:
    """Return the first element of a sequence safely if it exists."""
    if lst and len(lst) > 0:
        return lst[0]
    else:
        return None
