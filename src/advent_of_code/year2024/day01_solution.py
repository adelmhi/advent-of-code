from typing import Dict, List

from advent_of_code.utils.common import convert_to_int_matrix
from advent_of_code.utils.template import AOCSolution


def get_distance(list1: List[int], list2: List[int]) -> int:
    if len(list1) != len(list2):
        raise ValueError("Lists must be of equal length")

    list1_sorted = sorted(list1)
    list2_sorted = sorted(list2)

    # Store the distance between both list in a int variable
    distance = sum([abs(list1_sorted[i] - list2_sorted[i]) for i in range(len(list1))])
    return distance


def get_similarity(list1: List[int], list2: List[int]) -> int:
    # store in dict the number of occurance of number in list2
    dict2: Dict[int, int] = {}
    for num in list2:
        dict2[num] = dict2.get(num, 0) + 1

    similarity = sum([num * dict2.get(num, 0) for num in list1])
    return similarity


class Solution(AOCSolution):
    def __init__(self) -> None:
        super().__init__(year=2024, day=1)

    def part1(self, input_data: str) -> int:
        """Solve part 1 of the puzzle."""
        data = convert_to_int_matrix(input_data)
        list1 = [row[0] for row in data]
        list2 = [row[1] for row in data]
        return get_distance(list1, list2)

    def part2(self, input_data: str) -> int:
        """Solve part 2 of the puzzle."""
        data = convert_to_int_matrix(input_data)
        list1 = [row[0] for row in data]
        list2 = [row[1] for row in data]
        return get_similarity(list1, list2)


if __name__ == "__main__":
    solution = Solution()
    print(solution.solve())
