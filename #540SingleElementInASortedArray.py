"""
Given a sorted array consisting of only integers where every element appears twice except for one element which appears once. Find this single element that appears only once.

Example 1:
Input: [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:
Input: [3,3,7,7,10,11,11]
Output: 10
Note: Your solution should run in O(log n) time and O(1) space.
"""


class Solution(object):

    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        this funtion returns the element only appears once, with time complexity
         O(logn) and space complexity O(1).
        I want to use binary search. Each time divided the arrary into half.
        Check nums[mid] to determine wheter the single element is in the right
        side or in the left side. To avoid index out of range error, I will
        use r=n/2. n=len(nums)
        """
        if len(nums) == 1:
            return nums[0]
        l = 0
        r = len(nums) / 2
        while l < r:
            mid = l + (r - l) / 2
            if nums[2 * mid] == nums[2 * mid + 1]:
                l = l + 1
            else:
                r = mid
        return nums[2 * l]
