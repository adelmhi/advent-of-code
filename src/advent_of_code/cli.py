import argparse
import importlib
from pathlib import Path
from typing import Optional


def get_available_years() -> list:
    """Get list of available years from the directory structure."""
    base_path = Path(__file__).parent
    return [
        int(d.name[4:])
        for d in base_path.iterdir()
        if d.is_dir() and d.name.startswith("year")
    ]


def get_available_days(year: int) -> list:
    """Get list of available days for a given year."""
    base_path = Path(__file__).parent / f"year{year}"
    return [f.stem for f in base_path.glob("day*_solution.py")]


def run_solution(year: int, day: int, test_only: bool = False) -> None:
    """Run the solution for a specific day."""
    try:
        module_name = f"advent_of_code.year{year}.day{day:02d}_solution"
        solution_module = importlib.import_module(module_name)
        solution = solution_module.Solution()

        if test_only:
            part1_passed, part2_passed = solution.run_tests()
            if part1_passed and part2_passed:
                print("\nAll tests passed! 🎉")
            else:
                print("\nSome tests failed. 😢")
        else:
            part1, part2 = solution.solve()
            print(f"\nYear {year}, Day {day} Solutions:")
            print(f"Part 1: {part1}")
            print(f"Part 2: {part2}")

    except ImportError:
        print(f"Solution for {year} day {day} not found")
    except Exception as e:
        print(f"Error running solution: {str(e)}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Run Advent of Code solutions")
    parser.add_argument("--year", type=int, help="Year to run (e.g., 2024)")
    parser.add_argument("--day", type=int, help="Day to run (1-25)")
    parser.add_argument("--test", action="store_true", help="Run tests only")

    args = parser.parse_args()

    available_years = get_available_years()

    if not args.year:
        print("Available years:")
        for year in available_years:
            print(f"- {year}")
        return

    if args.year not in available_years:
        print(
            f"Year {args.year} not found. Available years: {', '.join(map(str, available_years))}"
        )
        return

    available_days = get_available_days(args.year)

    if not args.day:
        print(f"Available days for {args.year}:")
        for day in available_days:
            print(f"- {day}")
        return

    if args.day < 1 or args.day > 25:
        print("Day must be between 1 and 25")
        return

    run_solution(args.year, args.day, args.test)


if __name__ == "__main__":
    main()
