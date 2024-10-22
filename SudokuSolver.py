class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # define the necessary components of our sudoku board
        # digits = the input values
        # rows, cols, sub_grid keep track of the digits on the board
        digits = set({'1', '2', '3', '4', '5', '6', '7', '8', '9'})
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        sub_grid = [[set() for _ in range(3)] for _ in range(3)]


        # store empty cells in an array that we can fill later
        empty_cells = []


        # fill our sudoku board
        for r, row in enumerate(board):
            sub_r = int(r / 3)
            for c, cell in enumerate(row):
                sub_c = int(c / 3)
                if cell != ".":
                    rows[r].add(cell)
                    cols[c].add(cell)
                    sub_grid[sub_r][sub_c].add(cell)
                else:
                    empty_cells.append((r, c))
       
        #set a counter to see if solution is found
        self.solved = False


        def backtracking(cell_num):
            r, c = empty_cells[cell_num]
            sub_r = int(r/3)
            sub_c = int(c/3)


            # what options are available if all possible digits are picked
            # minus everything foind in rows, cols, and subgrid of the cell
            options = digits ^ (rows[r] | cols[c] | sub_grid[sub_r][sub_c])


            for op in options:
                rows[r].add(op)
                cols[c].add(op)
                sub_grid[sub_r][sub_c].add(op)
                board[r][c] = op


                # check if all empty_cells are finished
                if cell_num + 1 == len(empty_cells):
                    self.solved = True


                # if not solved, do the next job
                else:
                    backtracking(cell_num + 1)


                if self.solved:
                    return
               
                # remove wrong solutions
                rows[r].remove(op)
                cols[c].remove(op)
                sub_grid[sub_r][sub_c].remove(op)
                board[r][c] = "."
       
        backtracking(0)


       
