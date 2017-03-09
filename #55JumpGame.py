"""
55. Jump Game   Add to List QuestionEditorial Solution  My Submissions
Total Accepted: 107678
Total Submissions: 369094
Difficulty: Medium
Contributors: Admin
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.

Hide Company Tags Microsoft
Hide Tags Array Greedy
"""


class Solution(object):

    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        steps = 1
        for i in range(len(nums) - 1):
            steps -= 1
            if nums[i] == 0 and steps == 0:
                return False
            else:
                steps = max(nums[i], steps)
        return True
