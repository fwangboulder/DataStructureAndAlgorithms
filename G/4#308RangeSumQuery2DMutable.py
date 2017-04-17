"""
308. Range Sum Query 2D - Mutable Add to List
DescriptionHintsSubmissionsSolutions
Total Accepted: 13480
Total Submissions: 62937
Difficulty: Hard
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
update(3, 2, 2)
sumRegion(2, 1, 4, 3) -> 10
Note:
The matrix is only modifiable by the update function.
You may assume the number of calls to update and sumRegion function is distributed evenly.
You may assume that row1 ≤ row2 and col1 ≤ col2.
Hide Company Tags Google
Hide Tags Binary Indexed Tree Segment Tree
Hide Similar Problems (M) Range Sum Query 2D - Immutable (M) Range Sum Query - Mutable

"""
class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.d=matrix
        for row in matrix:
            for i in xrange(1,len(row)):
                row[i]+=row[i-1]


    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        row=self.d[row]
        orig=row[col]-(row[col-1] if col else 0)
        for i in xrange(col,len(row)):
            row[i]+=val-orig


    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        res=0
        for i in xrange(row1,row2+1):
            res+=self.d[i][col2]-(self.d[i][col1-1] if col1 else 0)
        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
