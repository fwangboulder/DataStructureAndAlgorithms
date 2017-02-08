"""
34. Search for a Range   Add to List QuestionEditorial Solution  My Submissions
Total Accepted: 117505
Total Submissions: 380413
Difficulty: Medium
Contributors: Admin
Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].

Hide Company Tags LinkedIn
Hide Tags Binary Search Array
Hide Similar Problems (E) First Bad Version

"""
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = -1
        right = -1
        if len(nums) == 0:
            return [left, right]

        start, end = 0, len(nums) - 1

        #search left
        #mid >= target, ends=mid
        while start + 1 < end:
            mid = start + (end - start) / 2
            if nums[mid] >= target:
                end = mid
            else:
                start = mid

        if nums[start] == target:
            left = start
        elif nums[end] == target:
            left = end
        else:
            #not found
            return [-1,-1]

        start, end = 0, len(nums) - 1
        #search right
        #mid <= target,start=mid
        while start + 1 < end:
            mid = start + (end-start)/2
            if nums[mid] <= target:
                start = mid
            else:
                end = mid

        if nums[end] == target:
            right = end
        elif nums[start] == target:
            right = start
        else:
            #not found
            return [-1, -1]

        return [left, right]
