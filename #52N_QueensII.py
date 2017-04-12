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

        path=[]
        res=[]
        index=0
        nums=[-1]*n
        self.dfs(nums,path,res,index)
        return len(res)
    def dfs(self,nums,path,res,index):
        if index==len(nums):

            res.append(path)
            return
        for i in xrange(len(nums)):
            nums[index]=i
            if self.isValid(nums,index):
                tmp="."*len(nums)
                self.dfs(nums,path+[tmp[:i]+"Q"+tmp[i+1:]],res,index+1)
    def isValid(self,nums,index):
        for i in xrange(index):
            if abs(nums[index]-nums[i])==index-i or nums[i]==nums[index]:
                return False
        return True

class Solution(object):

    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        stack = []
        for i in range(n):
            stack.append([(0, i)])

        while stack:
            board = stack.pop()
            row = len(board)
            if row == n:
                count += 1
            else:
                for col in range(n):
                    tmp = []
                    for r, c in board:
                        tmp.append(col != c and abs(col - c) != abs(row - r))
                    if all(tmp):
                        stack.append(board + [(row, col)])
        return count
