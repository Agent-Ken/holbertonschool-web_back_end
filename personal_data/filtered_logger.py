#!/usr/bin/env python3
'''
This module provides a function to obfuscate log messages.
'''

import re
from typing import List
import logging


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    '''Filtering values of certain fields in a log message'''
    for item in fields:
        message = re.sub(f"{item}=.*?{separator}",
                         f"{item}={redaction}{separator}", message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """A method for formatting for logs"""
        msg = filter_datum(self.fields, self.REDACTION,
                           record.getMessage(), self.SEPARATOR)
        return (self.FORMAT %
                {"name": record.name, "levelname": record.levelname, "asctime":
                 self.formatTime(record, self.datefmt), "message": msg})