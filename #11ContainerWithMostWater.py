"""
11. Container With Most Water   Add to List QuestionEditorial Solution  My Submissions
Total Accepted: 112542
Total Submissions: 311655
Difficulty: Medium
Contributors: Admin
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

Hide Company Tags Bloomberg
Hide Tags Array Two Pointers
Hide Similar Problems (H) Trapping Rain Water
"""


class Solution(object):

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start = 0
        end = len(height) - 1
        maxarea = 0
        while start < end:
            cur = (end - start)
            if height[start] < height[end]:
                cur = cur * height[start]
                start += 1
            else:
                cur = cur * height[end]
                end -= 1
            maxarea = max(cur, maxarea)
        return maxarea
