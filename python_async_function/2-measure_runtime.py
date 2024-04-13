#!/usr/bin/env python3

"""This module contains an asynchronous coroutine."""

import asyncio
import time

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the total execution time for wait_n."""
    start_time: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    elapsed_time: float = time.time() - start_time
    return elapsed_time / n
