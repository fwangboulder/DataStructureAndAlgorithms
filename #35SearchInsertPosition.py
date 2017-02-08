"""
35. Search Insert Position   Add to List QuestionEditorial Solution  My Submissions
Total Accepted: 140353
Total Submissions: 359829
Difficulty: Medium
Contributors: Admin
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0

Hide Tags Array Binary Search
Hide Similar Problems (E) First Bad Version
"""

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1

        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if nums[mid] >= target:
                #can not stop when equal because of possible duplicates, should continue search
                end = mid
            else:
                #start = mid + 1 is also fine
                start = mid

        #start, end, compare them with target, to find the right position
        if nums[start] >= target:
            return start
        if nums[end] >= target:
            return end
        #reach the end of array
        return len(nums)
