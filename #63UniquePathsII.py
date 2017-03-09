"""
63. Unique Paths II   Add to List QuestionEditorial Solution  My Submissions
Total Accepted: 90705
Total Submissions: 292511
Difficulty: Medium
Contributors: Admin
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.

Note: m and n will be at most 100.

Hide Company Tags Bloomberg
Hide Tags Array Dynamic Programming
Hide Similar Problems (M) Unique Paths

"""


class Solution(object):

    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        # O(m*n) space

        if not obstacleGrid:
            return
        r, c = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in xrange(c)] for _ in xrange(r)]
        dp[0][0] = 1 - obstacleGrid[0][0]
        for i in xrange(1, r):
            dp[i][0] = dp[i - 1][0] * (1 - obstacleGrid[i][0])
        for i in xrange(1, c):
            dp[0][i] = dp[0][i - 1] * (1 - obstacleGrid[0][i])
        for i in xrange(1, r):
            for j in xrange(1, c):
                dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) * \
                    (1 - obstacleGrid[i][j])
        return dp[-1][-1]
