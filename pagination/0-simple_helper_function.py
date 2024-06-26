#!/usr/bin/env python3
"""
This file contains function that  return
a tuple of size two containing a start index and an end index
corresponding to the range of indexes to return
in a list for those particular pagination parameters.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int]:
    '''method'''
    return ((page - 1) * page_size, page * page_size)
