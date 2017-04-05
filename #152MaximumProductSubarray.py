"""
152. Maximum Product Subarray Add to List
DescriptionSubmissionsSolutions
Total Accepted: 92043
Total Submissions: 369349
Difficulty: Medium
Contributors: Admin
Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.

Hide Company Tags LinkedIn
Hide Tags Array Dynamic Programming
Hide Similar Problems (E) Maximum Subarray (E) House Robber (M) Product of Array Except Self

"""


class Solution(object):

    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        MinTemp = nums[0]
        MaxTemp = nums[0]
        Max = nums[0]
        Min = nums[0]
        for i in xrange(1, len(nums)):
            MinTemp, MaxTemp = min(nums[i], nums[i] *
                                   MaxTemp, nums[i] *
                                   MinTemp), max(nums[i], nums[i] *
                                                 MaxTemp, nums[i] *
                                                 MinTemp)
            Max = max(Max, MaxTemp)
            Min = min(Min, MinTemp)
        print Max, Min
        return Max
