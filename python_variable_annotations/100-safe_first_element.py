#!/usr/bin/env python3
"""
This module provides a function to safely retrieve the first element of a sequence.
"""

from typing import Any, Optional, Sequence


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """Return the first element of a sequence or None if the sequence is empty."""
    if lst:
        return lst[0]
    else:
        return None
