#!/usr/bin/env python3
'''
This module provides a function to obfuscate log messages.
'''

import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    '''Filtering values of certain fields in a log message'''
    for item in fields:
        message = re.sub(f"{item}=.*?{separator}",
                         f"{item}={redaction}{separator}", message)
    return message
