import re
from typing import List

from advent_of_code.utils.template import AOCSolution


def extract_mult(corrupt_mem: str, with_do: bool = True) -> List[str]:
    if with_do:
        return re.findall(r"mul\(\d{1,3},\d{1,3}\)|do(?:n't)?\(\)", corrupt_mem)
    else:
        return re.findall(r"mul\(\d{1,3},\d{1,3}\)", corrupt_mem)


def get_mult_sum(corrupt_mem: str, with_do: bool = True) -> int:
    """
    Calculate the sum of all multiplication operations found in a corrupted memory string.

    The function looks for patterns of 'mul(x,y)' where x and y are 1-3 digit numbers,
    extracts these patterns using extract_mult(), and returns the sum of all x*y products.

    Args:
        corrupt_mem (str): A string containing corrupted memory data with multiplication operations

    Returns:
        int: The sum of all multiplication products found in the string

    Example:
        >>> get_mult_sum("mul(2,4)mul(3,7)")
        29  # (2*4 + 3*7 = 8 + 21 = 29)
    """
    mul_list = extract_mult(corrupt_mem, with_do)
    # By default, multiplication are enable at first
    enable = True
    mult_sum = 0
    for formul in mul_list:
        if formul == "don't()":
            enable = False
        elif formul == "do()":
            enable = True
        elif enable:
            numbers = re.search(r"(\d{1,3}),(\d{1,3})", formul)
            mult_sum += int(numbers.group(1)) * int(numbers.group(2))
    return mult_sum


class Solution(AOCSolution):
    def __init__(self) -> None:
        super().__init__(year=2024, day=3)  # Replace with the correct year and day

    def part1(self, input_data: str) -> int:
        """Solve part 1 of the puzzle."""
        return get_mult_sum(input_data, False)

    def part2(self, input_data: str) -> int:
        """Solve part 2 of the puzzle."""
        return get_mult_sum(input_data, True)


if __name__ == "__main__":
    solution = Solution()
    print(solution.solve())
