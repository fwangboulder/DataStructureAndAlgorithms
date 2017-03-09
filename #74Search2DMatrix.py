"""
74. Search a 2D Matrix
Description  Submission  Solutions  Add to List
Total Accepted: 110133
Total Submissions: 310430
Difficulty: Medium
Contributors: Admin
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.

Hide Tags Array Binary Search
Hide Similar Problems (M) Search a 2D Matrix II

"""


class Solution(object):

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        if not matrix[0]:
            return False
        m = len(matrix)
        n = len(matrix[0])
        total = m * n
        start = 0
        end = m * n - 1
        mid = start + (end - start) / 2
        while start + 1 < end:
            mid = start + (end - start) / 2

            if matrix[mid / n][mid % n] == target:
                return True
            elif matrix[mid / n][mid % n] < target:
                start = mid + 1
            else:
                end = mid
        if matrix[start / n][start % n] == target:
            return True
        if matrix[end / n][end % n] == target:
            return True

        return False
