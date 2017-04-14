"""
304. Range Sum Query 2D - Immutable Add to List
DescriptionHintsSubmissionsSolutions
Total Accepted: 29721
Total Submissions: 124512
Difficulty: Medium
Contributor: LeetCode
Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Range Sum Query 2D
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

Example:
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12
Note:
You may assume that the matrix does not change.
There are many calls to sumRegion function.
You may assume that row1 ≤ row2 and col1 ≤ col2.
Hide Tags Dynamic Programming
Hide Similar Problems (E) Range Sum Query - Immutable (H) Range Sum Query 2D - Mutable

"""
class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix=matrix
        self.dp=self.getDp(self.matrix)


    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if row1<0:
            s1=0
        else:
            s1=self.dp[row1][col2+1]
        if col2<0:
            s2=0
        else:
            s2=self.dp[row2+1][col1]
        if row1<0 or col1<0:
            s3=0
        else:
            s3=self.dp[row1][col1]
        return self.dp[row2+1][col2+1]-s1-s2+s3


    def getDp(self, matrix):
        if not matrix or not matrix[0]:
            return []
        m=len(matrix)
        n=len(matrix[0])
        #add one more dimension for corner cases
        dp=[[0 for _ in xrange(n+1)] for _ in xrange(m+1)]
        for i in xrange(1,m+1):
            for j in xrange(1,n+1):
                dp[i][j]=dp[i-1][j]+dp[i][j-1]-dp[i-1][j-1]+matrix[i-1][j-1]
        return dp







# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
