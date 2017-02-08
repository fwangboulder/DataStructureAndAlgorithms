"""
162. Find Peak Element   Add to List QuestionEditorial Solution  My Submissions
Total Accepted: 97351
Total Submissions: 270867
Difficulty: Medium
Contributors: Admin
A peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.

click to show spoilers.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.

Hide Company Tags Microsoft Google
Hide Tags Binary Search Array
"""
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 0:
            return

        if length == 1:
            return 0

        start, end = 0, length - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] < nums[mid - 1]:
                end = mid
            else:
                start = mid

        if nums[start] > nums[end]:
            return start
        else:
            return end
