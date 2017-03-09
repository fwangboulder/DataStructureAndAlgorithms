"""
37. Sudoku Solver   Add to List QuestionEditorial Solution  My Submissions
Total Accepted: 66428
Total Submissions: 234383
Difficulty: Hard
Contributors: Admin
Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'.

You may assume that there will be only one unique solution.


A sudoku puzzle...


...and its solution numbers marked in red.

Hide Company Tags Snapchat Uber
Hide Tags Backtracking Hash Table
Hide Similar Problems (M) Valid Sudoku

"""


class Solution(object):

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.solve(board)

    def solve(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for k in range(1, 10):
                        c = str(k)
                        if self.isValid(board, i, j, c):
                            board[i][j] = c
                            if self.solve(board):
                                return True
                            else:
                                board[i][j] = '.'
                    return False
        return True

    def isValid(self, board, row, col, c):

        for i in range(9):
            if board[i][col] == c:
                return False
            if board[row][i] == c:
                return False
            if board[3 * (row / 3) + i / 3][3 * (col / 3) + i % 3] == c:
                return False
        return True
