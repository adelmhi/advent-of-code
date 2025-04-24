import os
from pathlib import Path
from typing import Any, Optional

import requests
from dotenv import load_dotenv


def get_session_cookie() -> str:
    """
    Get the Advent of Code session cookie from environment variables or .env file.

    Returns:
        str: The session cookie value

    Raises:
        ValueError: If no session cookie is found
    """
    # Try to load from .env file first
    load_dotenv()

    # Check environment variables
    session = os.getenv("AOC_SESSION")
    if not session:
        raise ValueError(
            "No Advent of Code session cookie found. "
            "Please set the AOC_SESSION environment variable or add it to your .env file."
        )

    return session


def download_input(year: int, day: int) -> str:
    """
    Download input data from Advent of Code for a specific year and day.

    Args:
        year (int): The year of the puzzle
        day (int): The day of the puzzle
        session (str): The session cookie value

    Returns:
        str: The puzzle input as a string

    Raises:
        requests.RequestException: If the request fails
    """
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    cookies = {"session": get_session_cookie()}

    response = requests.get(url, cookies=cookies)
    response.raise_for_status()
    return response.text.strip()


def save_input_to_file(year: int, day: int, input_data: str) -> Path:
    """
    Save input data to a file in the inputs directory.

    Args:
        year (int): The year of the puzzle
        day (int): The day of the puzzle
        input_data (str): The input data to save

    Returns:
        Path: The path to the saved input file
    """
    # Create inputs directory if it doesn't exist
    inputs_dir = Path(__file__).parent.parent / "inputs" / f"year{year}"
    inputs_dir.mkdir(parents=True, exist_ok=True)

    # Save input to file
    input_file = inputs_dir / f"day{day:02d}_input.txt"
    input_file.write_text(input_data)

    return input_file


def get_input(year: int, day: int, force_download: bool = False) -> str:
    """
    Get input data for a specific year and day, either from cache or by downloading.

    Args:
        year (int): The year of the puzzle
        day (int): The day of the puzzle
        force_download (bool): Whether to force download even if cached

    Returns:
        str: The puzzle input as a string
    """
    # Check if input is already cached
    input_file = (
        Path(__file__).parent.parent
        / "inputs"
        / f"year{year}"
        / f"day{day:02d}_input.txt"
    )

    if not force_download and input_file.exists():
        return input_file.read_text().strip()

    # Download and cache the input
    input_data = download_input(year, day)
    save_input_to_file(year, day, input_data)

    return input_data


# def convert_to_int_matrix(data: str) -> List[List[int]]:
#     # Split the input into lines and remove any trailing whitespace
#     return [
#         [int(num) for num in line.split()]
#         for line in data.split('\n')
#     ]


def main() -> None:
    # Example usage
    year = 2024
    day = 1

    data = get_input(year, day)

    print("Print data:")
    print(f"{data[0:100]}...")


if __name__ == "__main__":
    main()
