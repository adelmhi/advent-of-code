from typing import List

from advent_of_code.utils.common import convert_to_int_matrix
from advent_of_code.utils.template import AOCSolution


def is_rate_safe(rate: int) -> bool:
    return rate > 0 and rate < 4


def is_report_safe(report: List[int]) -> bool:
    """
    Check if a report is safe by verifying that each number stricly increase/decrease
    and by increments smaller or equal to 3.

    Args:
        report (List[int]): List of integers representing the report values

    Returns:
        bool: True if the report is safe, False otherwise
    """
    # Exclude the singleton and empty cases
    if len(report) <= 1:
        return True

    # Get the direction of change between first two numbers (-1 for decrease, 1 for increase)
    diff = report[1] - report[0]
    if diff == 0:
        return False  # No change between consecutive numbers is not allowed
    sign = -1 if diff < 0 else 1

    for i in range(1, len(report)):
        rate = (report[i] - report[i - 1]) * sign
        if not is_rate_safe(rate):
            return False
    return True


def is_report_dampener_safe(report: List[int]) -> bool:
    """
    Check if a report is safe by verifying that each number stricly increase/decrease
    and by increments smaller or equal to 3. With dampener it's now possible to ignore
    a single level.

    Args:
        report (List[int]): List of integers representing the report values

    Returns:
        bool: True if the report is safe, False otherwise
    """
    # Exclude the singleton and empty cases
    if len(report) <= 2:
        return True

    ignored_level = []

    # Get the direction of change between first two numbers (-1 for decrease, 1 for increase)
    rates = [report[i] - report[i - 1] for i in range(1, len(report))]
    global_tendancy = sum(rates)
    sign = 1 if global_tendancy >= 0 else -1

    i = 1
    while i < len(report):
        crnt_rate = (report[i] - report[i - 1]) * sign
        if not is_rate_safe(crnt_rate):
            # Check if left number could be erased
            left_erasable = True
            if i > 1:
                prev_rate = (report[i - 1] - report[i - 2]) * sign
                left_erasable = is_rate_safe(prev_rate + crnt_rate)

            # Check if right number could be erased
            right_erasable = True
            if i < len(report) - 1:
                next_rate = (report[i + 1] - report[i]) * sign
                right_erasable = is_rate_safe(crnt_rate + next_rate)

            # Erase first right then left
            if right_erasable:
                ignored_level.append(report.pop(i))
            elif left_erasable:
                ignored_level.append(report.pop(i - 1))
            else:
                return False
        else:
            i += 1

    return len(ignored_level) <= 1


def get_safe_report_num(reports: List[List[int]]) -> int:
    return sum([int(is_report_safe(report)) for report in reports])


def get_dampener_safe_report_num(reports: List[List[int]]) -> int:
    return sum([int(is_report_dampener_safe(report)) for report in reports])


class Solution(AOCSolution):
    def __init__(self) -> None:
        super().__init__(year=2024, day=2)

    def part1(self, input_data: str) -> int:
        """Solve part 1 of the puzzle."""
        reports = convert_to_int_matrix(input_data)
        return get_safe_report_num(reports)

    def part2(self, input_data: str) -> int:
        """Solve part 2 of the puzzle."""
        reports = convert_to_int_matrix(input_data)
        return get_dampener_safe_report_num(reports)


if __name__ == "__main__":
    solution = Solution()
    print(solution.solve())
