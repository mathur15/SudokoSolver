class sudoko_solver:
    """
    Solve puzzle
    """
    def __init__(self, puzzle):
        self.puzzle = puzzle

    def is_valid(self):
        """
        Check if the puzzle is valid
        -> check entries
        -> size of boxes
        :param self: Puzzle
        :return: bool
        """
        size = self.puzzle.length()
        flag = True
        for row in self.puzzle:
            if row.length() < 9:
                flag = False
            else:
                for elements in row:
                    if elements not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
                        flag = False
        return size == 9 and flag == True

    def check_row(self, row, num):
        """
        :param row: row index to check
        :return: bool
        """
        length = len(self.puzzle)
        row = self.puzzle[row]

        for item in row:
            if item == num:
                return False
        return True
    def check_column(self, column, num):
        """
        :param column:
        :return: bool
        """
        # index to check in each sublist is the index corresponding to column
        for i in range(9):
            for j in range(9):
                if self.puzzle[i][column] == num:
                    return False
        return True

    def check_box(self,row,column,num):
        """
        :param row:
        :param column:
        :return:
        """
        for i in range(3):
            for j in range(3):
                if self.puzzle[row+i][j] == num:
                    return False
        return True

    def backtracking(self):
        """
        Implement the backtracking algorithm on the puzzle
        :param self:
        :return: bool
        """
if name == "__main__":

    #create it so that user inputs puzzle
    test_puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
                   [6, 0, 0, 1, 9, 5, 0, 0, 0],
                   [0, 9, 8, 0, 0, 0, 0, 6, 0],
                   [8, 0, 0, 0, 6, 0, 0, 0, 3],
                   [4, 0, 0, 8, 0, 3, 0, 0, 1],
                   [7, 0, 0, 0, 2, 0, 0, 0, 6],
                   [0, 6, 0, 0, 0, 0, 2, 8, 0],
                   [0, 0, 0, 4, 1, 9, 0, 0, 5],
                   [0, 0, 0, 0, 8, 0, 0, 7, 9]]
    solver_obj = sudoko_solver(test_puzzle)
    if solver_obj.is_valid():
        result = solver_obj.backtracking()
        if !result:
            print("No result found")







