import pytest

from advent_of_code.year2024.day01_solution import (
    Solution,
    get_distance,
    get_similarity,
)


def test_get_distance() -> None:
    assert get_distance([1, 2, 3], [4, 5, 6]) == 9
    assert get_distance([1, 1, 1], [1, 1, 1]) == 0
    assert get_distance([1, 2, 3], [3, 2, 1]) == 0


def test_get_similarity() -> None:
    assert get_similarity([1, 2, 3], [1, 2, 3]) == 6  # 1*1 + 2*1 + 3*1
    assert get_similarity([1, 1, 1], [1, 1, 1]) == 9
    assert get_similarity([1, 2, 3], [3, 2, 2]) == 7


def test_solution() -> None:
    solution = Solution()
    # Test with sample input
    input_data = """1 2\n2 3\n3 4"""
    assert solution.part1(input_data) == 3
    assert solution.part2(input_data) == 5
