"""
33. Search in Rotated Sorted Array   Add to List QuestionEditorial Solution  My Submissions
Total Accepted: 143134
Total Submissions: 446761
Difficulty: Medium
Contributors: Admin
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Hide Company Tags LinkedIn Bloomberg Uber Facebook Microsoft
Hide Tags Binary Search Array
Hide Similar Problems (M) Search in Rotated Sorted Array II (M) Find Minimum in Rotated Sorted Array

"""
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        start=0
        end=len(nums)-1
        while start+1<end:
            mid=start+(end-start)/2
            #left side is sorted
            if nums[mid]==target:
                return mid
            elif nums[mid]>nums[start]:
                if nums[start]<=target<nums[mid]:
                    end=mid
                else:
                    start=mid
            #right side is sorted
            else:
                if nums[mid]<target<=nums[end]:
                    start=mid
                else:
                    end=mid
        if nums[start]==target:
            return start
        elif nums[end]==target:
            return end
        else:
            return -1
