from typing import Dict, List, Tuple

from advent_of_code.utils.common import timed_execution
from advent_of_code.utils.template import AOCSolution


def parse_input(input_data: str) -> Tuple[List[Tuple[int, int]], List[List[int]]]:
    blocks = input_data.strip().split("\n\n")
    # Parse first block into list of tuples
    rules = []
    for line in blocks[0].split("\n"):
        a, b = map(int, line.split("|"))
        rules.append((a, b))
    # Parse second block into updates
    updates = []
    for line in blocks[1].split("\n"):
        updates.append(list(map(int, line.split(","))))
    return rules, updates


class OrderingRule:
    def __init__(self, orders: List[Tuple[int, int]]):
        self.orders = orders
        if not self.check_all_orders():
            raise ValueError(
                "Orders must contain all combinations of the number list without repetition"
            )

    def check_all_orders(self) -> bool:
        # get all numbers from orders
        number_list = []
        for order in self.orders:
            if order[0] not in number_list:
                number_list.append(order[0])
            if order[1] not in number_list:
                number_list.append(order[1])
        # Check if orders contains all combinations of the number list without repetition
        return len(self.orders) == len(number_list) * (len(number_list) - 1) // 2

    def get_update_dict(self, update: List[int]) -> Dict[int, int]:
        """Get the number of times a number should be after other numbers in the update"""
        update_dict = {num: 0 for num in update}
        for order in self.orders:
            a, b = order
            if a in update_dict and b in update_dict:
                update_dict[b] += 1
        return update_dict

    def check_update(self, update: List[int]) -> bool:
        # find the number of times a number should be after other numbers in the update
        update_dict = self.get_update_dict(update)
        for i in range(len(update) - 1):
            if update_dict[update[i]] > update_dict[update[i + 1]]:
                return False
        return True

    def get_correct_update(self, update: List[int]) -> List[int]:
        # find the number of times a number should be after other numbers in the update
        update_dict = self.get_update_dict(update)
        # sort the update by the number of times a number should be after other numbers
        return sorted(update, key=lambda x: update_dict[x])


class Solution(AOCSolution):
    def __init__(self) -> None:
        super().__init__(year=2024, day=5)

    @timed_execution
    def part1(self, input_data: str) -> int:
        """Solve part 1 of the puzzle."""
        rules, updates = parse_input(input_data)
        ordering_rule = OrderingRule(rules)
        total = 0
        for update in updates:
            if ordering_rule.check_update(update):
                total += update[len(update) // 2]
        return total

    @timed_execution
    def part2(self, input_data: str) -> int:
        """Solve part 2 of the puzzle."""
        rules, updates = parse_input(input_data)
        ordering_rule = OrderingRule(rules)
        total = 0
        for update in updates:
            correct_update = ordering_rule.get_correct_update(update)
            if update != correct_update:
                total += correct_update[len(update) // 2]
        return total


if __name__ == "__main__":
    solution = Solution()
    print(solution.solve())
