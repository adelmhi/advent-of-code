import sys
from pathlib import Path

# Add the src directory to PYTHONPATH
src_path = Path(__file__).parent / "src"
sys.path.append(str(src_path))

# Import and run the solution
from advent_of_code.year2024.day01_solution import Solution

if __name__ == "__main__":
    solution = Solution()
    print(solution.solve())
