"""
 Add to List
DescriptionSubmissionsSolutions
Total Accepted: 201558
Total Submissions: 377099
Difficulty: Easy
Contributors: Admin
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Hide Company Tags Palantir Airbnb
Hide Tags Hash Table Bit Manipulation
Hide Similar Problems (M) Single Number II (M) Single Number III (E) Missing Number (M) Find the Duplicate Number (E) Find the Difference

"""


class Solution(object):

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #[1,2,4,4,3,1,5]
        d = dict()
        for i in nums:
            d[i] = d.get(i, 0) + 1

        for i in d.keys():
            if d[i] == 1:
                return i

# method 2


class Solution(object):

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        for i in range(1, len(nums)):
            res = res ^ nums[i]
        return res
