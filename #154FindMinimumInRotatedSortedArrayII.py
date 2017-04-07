"""
154. Find Minimum in Rotated Sorted Array II Add to List
DescriptionSubmissionsSolutions
Total Accepted: 73058
Total Submissions: 199981
Difficulty: Hard
Contributors: Admin
Follow up for "Find Minimum in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array may contain duplicates.

Hide Tags Array Binary Search
Hide Similar Problems (M) Find Minimum in Rotated Sorted Array

"""


class Solution(object):

    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        start, end = 0, len(nums) - 1
        while start < end:
            mid = (start + end) / 2
            if nums[mid] > nums[end]:
                start = mid + 1
            elif nums[mid] < nums[end]:
                end = mid
            else:  # if nums[start] == nums[end], remove duplicates
                end -= 1
        return nums[end]
