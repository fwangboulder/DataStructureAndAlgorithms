"""
51. N-Queens   Add to List QuestionEditorial Solution  My Submissions
Total Accepted: 71134
Total Submissions: 243093
Difficulty: Hard
Contributors: Admin
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Hide Tags Backtracking
Hide Similar Problems (H) N-Queens II
"""

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        stack = []
        for i in range(n):
            stack.append([(0,i)]) # start stack: first row of board in four different columns
        while stack:
            board = stack.pop()
            row = len(board)
            #print 'b,r',board,row
            if row == n: # if there are four elements, this means one solution comes out
                tmpList = []
                for r,c in board:#row number stored in order
                    tmp = []
                    for i in range(n): #find the right column
                        if i == c:
                            tmp.append('Q')
                        else:
                            tmp.append('.')
                    tmp = ''.join(tmp)
                    tmpList.append(tmp)
                res.append(tmpList)
            for col in range(n):
                tmp = []
                for r, c in board:
                     #r=0,c=3,col!=3,col=0,1,2,row=1
                    #check whether vaild for each board element
                    tmp.append(col != c and abs(row-r) != abs(col-c))
                #print 'tmp', tmp
                if all(tmp):
                    stack.append(board+[(row, col)])
            #print 'end',stack,res
        return res
