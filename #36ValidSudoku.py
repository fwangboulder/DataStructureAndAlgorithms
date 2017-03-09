"""
36. Valid Sudoku   Add to List QuestionEditorial Solution  My Submissions
Total Accepted: 106364
Total Submissions: 311954
Difficulty: Medium
Contributors: Admin
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.


A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.

Hide Company Tags Snapchat Uber Apple
Hide Tags Hash Table
Hide Similar Problems (H) Sudoku Solver
"""


class Solution(object):

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        col = [{} for _ in range(9)]
        row = [{} for _ in range(9)]
        cell = [[{} for _ in range(3)] for _ in range(3)]
        for i in range(9):
            for j in range(9):
                n = board[i][j]
                if n == '.':
                    continue
                if n in row[i]:
                    return False
                else:
                    row[i][n] = [i, j]
                if n in col[j]:
                    return False
                else:
                    col[j][n] = [i, j]
                if n in cell[i / 3][j / 3]:
                    return False
                else:
                    cell[i / 3][j / 3][n] = [i, j]
        return True
