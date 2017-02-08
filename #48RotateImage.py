"""
48. Rotate Image   Add to List QuestionEditorial Solution  My Submissions
Total Accepted: 96349
Total Submissions: 258628
Difficulty: Medium
Contributors: Admin
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?

Hide Company Tags Amazon Microsoft Apple
Hide Tags Array
Have you met this question in a real interview? Yes
"""
# in place
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp

        for i in range(n):
            matrix[i] = matrix[i][::-1]
        
