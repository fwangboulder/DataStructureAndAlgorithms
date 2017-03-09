"""
80. Remove Duplicates from Sorted Array II
Description  Submission  Solutions  Add to List
Total Accepted: 104190
Total Submissions: 297373
Difficulty: Medium
Contributors: Admin
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.

Hide Company Tags Facebook
Hide Tags Array Two Pointers
"""


class Solution(object):

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return len(nums)
        tail = 1
        for i in range(2, len(nums)):
            if nums[tail] != nums[i] or nums[tail] != nums[tail - 1]:
                tail = tail + 1
                nums[tail] = nums[i]
        return tail + 1
