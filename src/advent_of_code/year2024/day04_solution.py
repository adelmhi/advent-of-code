from typing import List

from advent_of_code.utils.template import AOCSolution


def convert_to_xmas_matrix(string_grid: str) -> List[List[str]]:
    return [[letter for letter in line.split()[0]] for line in string_grid.split("\n")]


class XmasGrid:
    def __init__(self, string_grid: str) -> None:
        self.__grid = [
            [letter for letter in line.split()[0]] for line in string_grid.split("\n")
        ]
        self.__raw_count = len(self.__grid)
        self.__col_count = len(self.__grid[0])
        self.__search_word = "XMAS"

    def get_letter(
        self, x_pos: int, y_pos: int, x_offset: int = 0, y_offset: int = 0
    ) -> str:
        x_new = x_pos + x_offset
        y_new = y_pos + y_offset
        if (x_new < 0 or x_new > self.__col_count - 1) or (
            y_new < 0 or y_new > self.__raw_count - 1
        ):
            return ""
        return self.__grid[y_new][x_new]

    def check_word_from_direction(
        self, x_pos: int, y_pos: int, vect_x: int, vect_y: int
    ) -> bool:
        # exclude case where no movement
        if vect_x == 0 and vect_y == 0:
            return False

        if vect_x not in [-1, 0, 1] and vect_y not in [-1, 0, 1]:
            vect_x = int(vect_x / abs(vect_x))
            vect_y = int(vect_y / abs(vect_y))

        search_idx = 0
        while search_idx != len(self.__search_word):
            if (
                self.get_letter(x_pos, y_pos, search_idx * vect_x, search_idx * vect_y)
                != self.__search_word[search_idx]
            ):
                return False
            search_idx += 1
        return True

    def check_for_x_mas(self, x_pos: int, y_pos: int, vect_x: int, vect_y: int) -> bool:
        middle_letter = "A"
        to_vector_letter = "M"
        from_vector_letter = "S"

        # Get sign of transformation
        sgn = vect_x * vect_y

        return (
            self.get_letter(x_pos, y_pos) == middle_letter
            and self.get_letter(x_pos, y_pos, vect_x, vect_y) == to_vector_letter
            and self.get_letter(x_pos, y_pos, -sgn * vect_x, sgn * vect_y)
            == to_vector_letter
            and self.get_letter(x_pos, y_pos, sgn * vect_x, -sgn * vect_y)
            == from_vector_letter
            and self.get_letter(x_pos, y_pos, -vect_x, -vect_y) == from_vector_letter
        )

    def get_wordshape_count(self) -> int:
        wordshape_count = 0
        for y_pos in range(self.__col_count):
            for x_pos in range(self.__raw_count):
                for vect_x in [-1, 1]:
                    for vect_y in [-1, 1]:
                        if self.check_for_x_mas(x_pos, y_pos, vect_x, vect_y):
                            wordshape_count += 1
        return wordshape_count

    def get_word_count(self) -> int:
        word_count = 0
        for y_pos in range(self.__col_count):
            for x_pos in range(self.__raw_count):
                for vect_y in [-1, 0, 1]:
                    for vect_x in [-1, 0, 1]:
                        if self.check_word_from_direction(x_pos, y_pos, vect_x, vect_y):
                            word_count += 1
        return word_count


class Solution(AOCSolution):
    def __init__(self) -> None:
        super().__init__(year=2024, day=4)  # Replace with the correct year and day

    def part1(self, input_data: str) -> int:
        """Solve part 1 of the puzzle."""
        xmas_grid = XmasGrid(input_data)
        return xmas_grid.get_word_count()

    def part2(self, input_data: str) -> int:
        """Solve part 2 of the puzzle."""
        xmas_grid = XmasGrid(input_data)
        return xmas_grid.get_wordshape_count()


if __name__ == "__main__":
    solution = Solution()
    print(solution.solve())
