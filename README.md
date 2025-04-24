# Advent of Code Solutions

This repository contains my solutions to the Advent of Code challenges, organized by year and day.

## Project Structure

```
advent_of_code/
├── src/                      # Source code root
│   └── advent_of_code/      # Main package
│       ├── utils/           # Utility functions and templates
│       │   ├── aoc_login.py # Session management for AOC
│       │   ├── template.py  # Base solution template
│       │   └── common.py    # Common utility functions
│       ├── year2024/        # Solutions for 2024
│       │   ├── day01_solution.py
│       │   └── ...
│       ├── year2023/        # Solutions for 2023
│       │   └── ...
│       └── cli.py           # Command-line interface
├── inputs/                  # Input files
│   ├── year2024/
│   └── year2023/
├── tests/                   # Test files
│   ├── year2024/
│   └── year2023/
├── pyproject.toml          # Modern Python packaging configuration
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## Setup

1. Clone this repository:
```bash
git clone <repository-url>
cd advent_of_code
```

2. Create and activate a virtual environment (recommended):
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/MacOS
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up your Advent of Code session cookie:
   - Log in to [Advent of Code](https://adventofcode.com)
   - Copy your session cookie from your browser
   - Create a `.env` file in the root directory with:
     ```
     AOC_SESSION=your_session_cookie_here
     ```

5. Install the package in development mode:
```bash
pip install -e .
```

## Usage

### Using the CLI

The project includes a command-line interface to run solutions:

```bash
# List available years
aoc

# List available days for a specific year
aoc --year 2024

# Run a specific solution
aoc --year 2024 --day 1

# Run tests for a solution
aoc --year 2024 --day 1 --test
```

### Running Solutions Directly

You can also run solutions directly:

```bash
# Using the run script (recommended)
python run.py

# Or run a specific solution file
python src/advent_of_code/year2024/day01_solution.py
```

## Creating New Solutions

1. Create a new solution file in the appropriate year directory:
   ```bash
   cp src/advent_of_code/utils/template.py src/advent_of_code/year2024/dayXX_solution.py
   ```

2. Update the class name and implement the `part1` and `part2` methods:
   ```python
   class DayXXSolution(AOCSolution):
       def __init__(self):
           super().__init__(year=2024, day=XX)
       
       def part1(self, input_data: str) -> int:
           # Implement part 1 solution
           pass
       
       def part2(self, input_data: str) -> int:
           # Implement part 2 solution
           pass
   ```

3. Add test cases in the `tests` directory:
   ```bash
   mkdir -p tests/year2024
   touch tests/year2024/dayXX_tests.json
   ```

4. Test your solution:
   ```bash
   aoc --year 2024 --day XX --test
   ```

## Development Tools

The project includes several development tools configured in `pyproject.toml`:

- `black` for code formatting
- `isort` for import sorting
- `mypy` for type checking
- `pytest` for testing

To use these tools:

```bash
# Install development dependencies
pip install -e ".[dev]"

# Format code
black .
isort .

# Run type checking
mypy .

# Run tests
pytest
```

## Contributing

Feel free to submit issues or pull requests with improvements or additional solutions. 