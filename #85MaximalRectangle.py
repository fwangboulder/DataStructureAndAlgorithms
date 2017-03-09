"""
85. Maximal Rectangle Add to List
Description  Submission  Solutions
Total Accepted: 58881
Total Submissions: 222734
Difficulty: Hard
Contributors: Admin
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 6.
Hide Company Tags Facebook
Hide Tags Array Hash Table Stack Dynamic Programming
Hide Similar Problems (H) Largest Rectangle in Histogram (M) Maximal Square

"""
# convert two dimension to one dimension and then do the same as #84


class Solution(object):

    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        res = 0
        n = len(matrix[0])
        heights = [0] * (n + 1)
        for row in matrix:
            for i in xrange(n):
                if row[i] == '1':
                    heights[i] += 1
                else:
                    heights[i] = 0
            stack = [-1]
            for i in xrange(n + 1):
                while heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i - stack[-1] - 1
                    res = max(res, h * w)
                stack.append(i)
        return res
