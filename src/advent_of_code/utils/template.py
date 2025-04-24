import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, List, Optional, Tuple

import requests

from .aoc_login import get_input


@dataclass
class TestCase:
    """Represents a test case with input and expected output."""

    input_data: str
    expected_part1: Optional[Any] = None
    expected_part2: Optional[Any] = None
    description: Optional[str] = None


class AOCSolution:
    def __init__(self, year: int, day: int):
        self.year = year
        self.day = day

    def part1(self, input_data: str) -> int:
        """Solve part 1 of the puzzle."""
        raise NotImplementedError("Part 1 not implemented")

    def part2(self, input_data: str) -> int:
        """Solve part 2 of the puzzle."""
        raise NotImplementedError("Part 2 not implemented")

    def solve(self) -> Tuple[int, int]:
        """Solve both parts of the puzzle."""
        input_data = get_input(self.year, self.day)
        return self.part1(input_data), self.part2(input_data)

    def _load_test_cases(self) -> List[TestCase]:
        """Load test cases from JSON file."""
        test_file = (
            Path(__file__).parent.parent
            / "tests"
            / f"year{self.year}"
            / f"day{self.day:02d}_tests.json"
        )

        if not test_file.exists():
            return []

        with open(test_file, "r") as f:
            test_data = json.load(f)

        return [
            TestCase(
                input_data=case["input"],
                expected_part1=case.get("part1"),
                expected_part2=case.get("part2"),
                description=case.get("description"),
            )
            for case in test_data
        ]

    def run_tests(self) -> Tuple[bool, bool]:
        """
        Run all test cases for this solution.

        Returns:
            Tuple[bool, bool]: (part1_passed, part2_passed)
        """
        test_cases = self._load_test_cases()
        if not test_cases:
            print(f"No test cases found for {self.year} day {self.day}")
            return True, True  # Consider no tests as passed

        part1_passed = True
        part2_passed = True

        for i, test_case in enumerate(test_cases, 1):
            print(f"\nTest Case {i}: {test_case.description or 'No description'}")

            # Test Part 1
            if test_case.expected_part1 is not None:
                try:
                    result = self.part1(test_case.input_data)
                    if result == test_case.expected_part1:
                        print(
                            f"✓ Part 1: {result} (expected: {test_case.expected_part1})"
                        )
                    else:
                        print(
                            f"✗ Part 1: {result} (expected: {test_case.expected_part1})"
                        )
                        part1_passed = False
                except Exception as e:
                    print(f"✗ Part 1 failed with error: {str(e)}")
                    part1_passed = False

            # Test Part 2
            if test_case.expected_part2 is not None:
                try:
                    result = self.part2(test_case.input_data)
                    if result == test_case.expected_part2:
                        print(
                            f"✓ Part 2: {result} (expected: {test_case.expected_part2})"
                        )
                    else:
                        print(
                            f"✗ Part 2: {result} (expected: {test_case.expected_part2})"
                        )
                        part2_passed = False
                except Exception as e:
                    print(f"✗ Part 2 failed with error: {str(e)}")
                    part2_passed = False

        return part1_passed, part2_passed
