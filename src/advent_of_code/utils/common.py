import re
from pathlib import Path
from typing import Any, Callable, List


def convert_to_int_matrix(data: str) -> List[List[int]]:
    """Convert a string of numbers into a matrix of integers."""
    return [[int(num) for num in line.split()] for line in data.split("\n")]


def read_input_file(file_path: str) -> List[str]:
    """Read input from a file."""
    with open(file_path, "r") as f:
        return [line.strip() for line in f.readlines()]


def extract_numbers(text: str) -> List[int]:
    """Extract all numbers from a string."""
    return list(map(int, re.findall(r"-?\d+", text)))


def timed_execution(func: Callable) -> Callable:
    """Decorator to measure execution time of a function."""
    import time

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {(end_time - start_time)*1e+3:.4f} ms")
        return result

    return wrapper


def memoize(func: Callable) -> Callable:
    """Decorator to cache function results."""
    cache = {}

    def wrapper(*args: Any) -> Any:
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrapper
