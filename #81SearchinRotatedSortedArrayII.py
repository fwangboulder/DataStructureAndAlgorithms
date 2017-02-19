"""
Description  Submission  Solutions
Total Accepted: 84629
Total Submissions: 257389
Difficulty: Medium
Contributors: Admin
Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Write a function to determine if a given target is in the array.

The array may contain duplicates.

Subscribe to see which companies asked this question.

Hide Tags Array Binary Search
Hide Similar Problems (M) Search in Rotated Sorted Array

"""
class Solution(object):
    def search(self,nums,target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
       length = len(nums)
        if length == 0:
            return False

        start, end = 0, length - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if target == nums[mid]:
                return True

            if nums[start] < nums[mid]:
                #left is sorted
                if nums[start] <= target and target < nums[mid]:
                    end = mid
                else:
                    start = mid
            elif nums[start]==nums[mid]:  ####duplicate case
                start+=1
            else:
                #right is sorted
                if target > nums[mid] and target <= nums[end]:
                    start = mid
                else:
                    end = mid

        if nums[start] == target:
            return True
        if nums[end] == target:
            return True
        return False
