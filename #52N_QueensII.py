"""
52. N-Queens II   Add to List QuestionEditorial Solution  My Submissions
Total Accepted: 56890
Total Submissions: 132331
Difficulty: Hard
Contributors: Admin
Follow up for N-Queens problem.

Now, instead outputting board configurations, return the total number of distinct solutions.



Hide Company Tags Zenefits
Hide Tags Backtracking
Hide Similar Problems (H) N-Queens
"""

class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        count=0
        stack=[]
        for i in range(n):
            stack.append([(0,i)])

        while stack:
            board=stack.pop()
            row=len(board)
            if row==n:
                count+=1
            else:
                for col in range(n):
                    tmp=[]
                    for r,c in board:
                        tmp.append(col!=c and abs(col-c)!=abs(row-r))
                    if all(tmp):
                        stack.append(board+[(row,col)])
        return count
        
