"""
137. Single Number II Add to List
DescriptionSubmissionsSolutions
Total Accepted: 110712
Total Submissions: 272725
Difficulty: Medium
Contributors: Admin
Given an array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Hide Tags Bit Manipulation
Hide Similar Problems (E) Single Number (M) Single Number III
"""


class Solution(object):

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1
        for i in d.keys():
            if d[i] != 3:
                return i
# method 2: bit manipulation.


class Solution(object):

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ones = 0
        twos = 0
        threes = 0
        for i in xrange(len(nums)):
            # twos holds the number appears twice
            twos |= ones & nums[i]
            # ones holds the number appears once
            ones ^= nums[i]

            # threes holds the number appears three times
            threes = ones & twos
            # if nums[i] appears three times, doing this will clear ones and
            # twos
            ones &= ~threes
            twos &= ~threes
        return ones
