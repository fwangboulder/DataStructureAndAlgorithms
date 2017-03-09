"""
41. First Missing Positive   Add to List QuestionEditorial Solution  My Submissions
Total Accepted: 86768
Total Submissions: 347450
Difficulty: Hard
Contributors: Admin
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.

Hide Tags Array
Hide Similar Problems (E) Missing Number (M) Find the Duplicate Number (E) Find All Numbers Disappeared in an Array
"""


class Solution(object):

    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = 0, len(nums) - 1
        while start <= end:
            index = nums[start] - 1
            if index == start:
                start += 1
            # nums[start] is not valid, moves nums[end] to start, end-=1
            elif index < 0 or index > end or nums[start] == nums[index]:
                nums[start] = nums[end]
                end -= 1
            else:  # swap nums[start] and nums[index]
                nums[start] = nums[index]
                nums[index] = index + 1
        return start + 1
