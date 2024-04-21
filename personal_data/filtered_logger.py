#!/usr/bin/env python3
"""
This module provides a function to obfuscate
log messages.
"""

import re


def filter_datum(fields: list, redaction: str,
                 message: str, separator: str) -> str:
    """
    Obfuscate the values of certain fields in
    a log message.
    """
    for field in fields:
        message = re.sub(f"{field}=[^;]*",
                         f"{field}={redaction}", message)
    return message
