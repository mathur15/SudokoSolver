import UI_grid as grid


class SudokuSolver:
    """
    Solve puzzle
    """
    def __init__(self, puzzle):
        self.puzzle = puzzle
        grid.make_grid(self.puzzle)

    def is_valid(self):
        """
        Check if puzzle is valid
        """
        size = len(self.puzzle)
        flag = True
        for row in self.puzzle:
            if len(row) < 9:
                flag = False
            else:
                for elements in row:
                    if elements not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
                        flag = False
        return size == 9 and flag is True

    def check_row(self, row, num):
        """
        Check if row already consists of num.
        """
        length = len(self.puzzle)
        row = self.puzzle[row]

        for item in row:
            if item == num:
                return False
        return True

    def check_column(self, column, num):
        """
        Check if column already consists of num.
        """
        # index to check in each sublist is the index corresponding to column
        for i in range(9):
            for j in range(9):
                if self.puzzle[i][column] == num:
                    return False
        return True

    def check_box(self, row, column, num):
        """
        Check box if num already exists in 3x3 box
        """
        start_i_j = self.find_start(row, column)
        start_row = start_i_j[0]
        start_column = start_i_j[1]
        for i in range(3):
            for j in range(3):
                if self.puzzle[start_row+i][start_column+j] == num:
                    return False
        return True

    def find_open_location(self):
        """
        Find the first occurring row and column index where there is a 0
        """
        position = []
        count = 0
        for i in range(9):
            for j in range(9):
                if self.puzzle[i][j] == 0 and count == 0:
                    position.append(i)
                    position.append(j)
                    count = count + 1
        return position

    def find_start(self, row, column):
        """
        Return the starting row and column index for the box the element
        belongs to.
        """
        start_of_box = []
        row_start_index = row % 3
        column_start_index = column % 3
        start_of_box.append(row-row_start_index)
        start_of_box.append(column-column_start_index)
        return start_of_box

    def backtracking(self):
        """
        Implement the backtracking algorithm on the puzzle
        """
        position = self.find_open_location()
        if not position:
            return True
        else:
            row_index = position[0]
            column_index = position[1]

        # try all possible numbers
        for i in range(1, 10):
            if self.check_row(row_index, i) and self.check_column(column_index, i) \
                    and self.check_box(row_index, column_index, i):
                    self.puzzle[row_index][column_index] = i
                    if self.backtracking():
                        return True
                    self.puzzle[row_index][column_index] = 0
        return False

    def output_result(self):
        """
        Output final grid
        """
        grid.make_grid(self.puzzle)


if __name__ == "__main__":
    test_puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
                   [6, 0, 0, 1, 9, 5, 0, 0, 0],
                   [0, 9, 8, 0, 0, 0, 0, 6, 0],
                   [8, 0, 0, 0, 6, 0, 0, 0, 3],
                   [4, 0, 0, 8, 0, 3, 0, 0, 1],
                   [7, 0, 0, 0, 2, 0, 0, 0, 6],
                   [0, 6, 0, 0, 0, 0, 2, 8, 0],
                   [0, 0, 0, 4, 1, 9, 0, 0, 5],
                   [0, 0, 0, 0, 8, 0, 0, 7, 9]]
    solver_obj = SudokuSolver(test_puzzle)
    if solver_obj.is_valid():
        result = solver_obj.backtracking()
        solver_obj.output_result()







