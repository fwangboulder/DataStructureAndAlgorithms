"""
361. Bomb Enemy Add to List
DescriptionHintsSubmissionsSolutions
Total Accepted: 13523
Total Submissions: 35074
Difficulty: Medium
Contributor: LeetCode
Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero), return the maximum enemies you can kill using one bomb.
The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since the wall is too strong to be destroyed.
Note that you can only put the bomb at an empty cell.

Example:
For the given grid

0 E 0 0
E 0 W E
0 E 0 0

return 3. (Placing a bomb at (1,1) kills 3 enemies)
Credits:
Special thanks to @memoryless for adding this problem and creating all test cases.

Hide Company Tags Google
Hide Tags Dynamic Programming

"""
class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int

        """
        if not grid or not grid[0]:
            return 0
        def killed_rows(g):
            m,n=len(g),len(g[0])
            kills=[[0]*n for i in range(m)]
            for i in range(m):
                s=count=0
                for j in range(n+1):
                    if j==n or g[i][j]=='W':
                        for k in range(s,j):
                            if g[i][k]=='0':
                                kills[i][k]=count
                        s=j+1
                        count=0
                    elif g[i][j]=='E':
                        count+=1
            return kills
        hs,vs=killed_rows(grid),killed_rows(zip(*grid))
        return max(hs[i][j]+vs[j][i] for i in range(len(hs)) for j in range(len(vs)))


class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        m,n = len(grid),len(grid[0])
        def count(i,j,di,dj):
            cnt = 0
            while i < m and j < n and grid[i][j] != 'W':
                cnt += 1 if grid[i][j]=='E' else 0
                i += di
                j += dj
            return cnt
        dp,ans = [0]*n,0
        for i in xrange(m):
            for j in xrange(n):
                up,left = grid[i-1][j] if i > 0 else 'W',grid[i][j-1] if j > 0 else 'W'
                cx = dp[j-1][0] if left != 'W' else count(i,j,0,1)
                cy = dp[j][1] if up != 'W' else count(i,j,1,0)
                dp[j] = (cx,cy)
                if grid[i][j]=='0':
                    ans = max(ans,cx+cy)
        return ans
