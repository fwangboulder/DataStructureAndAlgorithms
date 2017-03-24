"""
130. Surrounded Regions Add to List
DescriptionSubmissionsSolutions
Total Accepted: 75541
Total Submissions: 424071
Difficulty: Medium
Contributors: Admin
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Hide Tags Breadth-first Search Union Find
Hide Similar Problems (M) Number of Islands (M) Walls and Gates
bfs
"""


class Solution(object):

    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # BFS
        queue = collections.deque([])
        # put all 0 in the edge into queue
        for r in xrange(len(board)):
            for c in xrange(len(board[0])):
                if (r in [0, len(board) - 1] or c in [0,
                                                      len(board[0]) - 1]) and board[r][c] == "O":
                    queue.append((r, c))
        while queue:
            # change all the '0' connected to edge 0 (included) to D
            r, c = queue.popleft()
            if 0 <= r < len(board) and 0 <= c < len(
                    board[0]) and board[r][c] == "O":
                board[r][c] = "D"
                queue.append((r - 1, c))
                queue.append((r + 1, c))
                queue.append((r, c - 1))
                queue.append((r, c + 1))
        # change all 'D' to '0' and all '0' to 'X'
        for r in xrange(len(board)):
            for c in xrange(len(board[0])):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "D":
                    board[r][c] = "O"
