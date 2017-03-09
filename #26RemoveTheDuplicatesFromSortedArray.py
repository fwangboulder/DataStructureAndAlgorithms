"""
26. Remove Duplicates from Sorted Array   Add to List QuestionEditorial Solution  My Submissions
Total Accepted: 191818
Total Submissions: 543304
Difficulty: Easy
Contributors: Admin
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.

Hide Company Tags
"""


class Solution(object):

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        start = 0
        while start < len(nums) - 1:
            if nums[start] == nums[start + 1]:
                l -= 1
                print start + 2, nums[:start + 1], nums[start + 2:]
                nums = nums[:start + 1] + nums[start + 2:]


class Solution(object):

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) <= 1:
            return len(nums)
        else:
            head, tail = 1, 0
            while head < len(nums):
                if nums[head] == nums[tail]:
                    head += 1
                elif head - tail == 1:
                    tail, head = tail + 1, head + 1
                else:
                    nums[tail + 1] = nums[head]
                    tail, head = tail + 1, head + 1
        return tail + 1

            start += 1

        return l
