#! /usr/bin/env python
import unittest

"""
Search for a Range(#34)
Given a sorted array, find the start and end position of a given target value.

example: [5,7,7,8,8,10] return [3,4]
if not found, return [-1,-1]


Search insert position(#35)
Given a sorted array and a target value, return the index if the target is found.
if not, return the index where it would be it were inserted in order.
example:
[1,3,5,6], 5 -> 2
"""


class Solution(object):

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        this function produces the index range of target. If not found, return [-1,-1]

        I want to use two pointers, start=0 and end=len(nums)-1,
        then compare the mid=start+(end-start)/2 value (nums[mid]) with target, and shift the pointer position.
        Continue to do this until start+1<end or both nums[start] and nums[end] equal to target.
        Since each time half of the elements are ignored, the time complexity is O(logn).The space complexity is
        O(1)
        """
        if not nums:
            return [-1, -1]
        start = 0
        end = len(nums) - 1
        index1 = -1
        index2 = -1
        # find the left bound of target
        while start + 1 < end:  # avoid dead loop
            mid = start + (end - start) / 2  # avoid exceed value limit
            if nums[mid] > target:
                end = mid
            elif nums[mid] < target:
                start = mid
            else:
                end = mid

        if nums[start] == target:
            index1 = start
        elif nums[end] == target:
            index1 = end

        # find right bound of target
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if nums[mid] > target:
                end = mid
            elif nums[mid] < target:
                start = mid
            else:
                start = mid
        if nums[end] == target:
            index2 = end
        elif nums[start] == target:
            index2 = start

        return [index1, index2]

    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        this function produces the position of the target, if the target not found, return the
        insert position which keep the nums in order.
        In another word, this is a problem to find the first value equal or bigger than the target valueand
        then return the index. I can use the two pointers and get rid of half part of elements by comparision of values for
        target and mid=start+(end-start)/2. The time complexity is O(logn) and the space complexity is O(1).
        """
        if not nums:
            return 0
        # check the case that target is the smallest or largest value
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if nums[mid] > target:
                end = mid
            elif nums[mid] < target:
                start = mid
            else:
                end = mid  # the first value equal or larger than target
        if nums[start] >= target:
            return start
        if nums[end] >= target:
            return end


# test
case = Solution()


class test(unittest.TestCase):

    def test_searchRange(self):
        self.assertEqual(case.searchRange([5, 7, 7, 8, 8, 10], 8), [3, 4])
        self.assertEqual(case.searchRange([5, 7, 7, 8, 8, 10], 0), [-1, -1])

    def test_searchInsert(self):
        self.assertEqual(case.searchInsert([1], 2), 1)
        self.assertEqual(case.searchInsert([2], 2), 0)
        self.assertEqual(case.searchInsert([1, 2, 4], 3), 2)
        self.assertEqual(case.searchInsert([1, 2, 2, 4], 2), 1)



if __name__ == "__main__":
    unittest.main()
