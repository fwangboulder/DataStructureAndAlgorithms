"""
64. Minimum Path Sum   Add to List QuestionEditorial Solution  My Submissions
Total Accepted: 98858
Total Submissions: 264928
Difficulty: Medium
Contributors: Admin
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Hide Tags Array Dynamic Programming
Hide Similar Problems (M) Unique Paths (H) Dungeon Game
Have you met this question in a real interview? Yes

"""


class Solution(object):

    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        用动态规划解题
        到达dp[i][j]有两种途径：dp[i-1][j]+grid[i][j] or dp[i][j-1]+grid[i][j]
        start dp[0][0]=grid[0][0]
        if i==0: dp[i][j]=dp[i][j-1]+grid[i][j]
        if j==0: dp[i][j]=dp[i-1][j]+grid[i][j]
        we need dp[m-1][n-1]

        """
        m = len(grid)
        n = len(grid[0])
        dp = [0 for col in range(n)]
        print dp
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[j] = grid[i][j]
                elif i == 0 and j != 0:
                    dp[j] = dp[j - 1] + grid[i][j]
                elif j == 0 and i != 0:
                    dp[j] = dp[j] + grid[i][j]
                else:
                    dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]
        return dp[n - 1]
