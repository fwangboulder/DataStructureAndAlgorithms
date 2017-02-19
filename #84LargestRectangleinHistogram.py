"""
84. Largest Rectangle in Histogram Add to List
Description  Submission  Solutions
Total Accepted: 81726
Total Submissions: 316426
Difficulty: Hard
Contributors: Admin
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].


The largest rectangle is shown in the shaded area, which has area = 10 unit.

For example,
Given heights = [2,1,5,6,2,3],
return 10.

Hide Tags Array Stack
Hide Similar Problems (H) Maximal Rectangle

#use a stack to store a ascending value index, if decrese,pop out the top value.

"""

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        stack=[-1]
        res=0
        for i in xrange(len(heights)):
            while heights[i]<heights[stack[-1]]:
                h=heights[stack.pop()]
                w=i-stack[-1]-1
                res=max(res,h*w)

            stack.append(i)
        return res
