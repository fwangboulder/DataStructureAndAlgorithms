"""
153. Find Minimum in Rotated Sorted Array Add to List
DescriptionSubmissionsSolutions
Total Accepted: 139069
Total Submissions: 355579
Difficulty: Medium
Contributors: Admin
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.

Hide Company Tags Microsoft
Hide Tags Array Binary Search
Hide Similar Problems (M) Search in Rotated Sorted Array (H) Find Minimum in Rotated Sorted Array II

"""


class Solution(object):

    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        This function provides the minimum of the rotated array. One solution can
        be loop the array and find a value nums[i], so that nums[i]<nums[i+1] and
        nums[i]<nums[i-1]. The edge condition is the minimum is the first element or
        the last element.
        The time complexity is O(n) and the space complexity is O(1).
        If I want to reduce the time complexity. I can use two pointers and perfom the binary
        search method. start=0, end=len(nums)-1, mid=start+(end-start)/2
        nums[start]<nums[mid], then start=mid
        nums[start]>nums[mid], then  end=mid
        The time complexity is O(logn) and the space complexity is O(1)

        """
        if not nums:
            return 'nums is empty'
        start = 0
        end = len(nums) - 1
        # only one element or no rotation
        if nums[0] <= nums[-1]:
            return nums[0]
        while start + 1 < end:
            mid = start + (end - start) / 2
            if nums[mid] > nums[start]:
                start = mid
            else:
                end = mid
        if nums[start] < nums[end]:
            return nums[start]
        else:
            return nums[end]
