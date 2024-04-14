#!/usr/bin/env python3
"""program to return the first 
element of a sequence if it's not empty.
"""

from typing import Sequence, Any, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """Return the first element 
    of a sequence if it's not empty.
    """
    if lst:
        return lst[0]
    return None
