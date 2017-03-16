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

Search a 2D Matrix (#74) for a target value
Given a 2D matrix: integers in each row are sorted from left to right; the first integer is always
larger than the last integer in previous row.

Search a 2D Matrix II (#240)
Given a 2D matrix: integers in each row are sorted for each row and each column, which means the
first integer might be smaller than the last integer in previous row.

First Bad Version (#278)
Given n versions [1,...,n], find the first bad version.
API calls: bool isBadVersion(version), minimize the number of calls for this API.

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

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        This function produces whether the matrix contains the target. Notice the matrix
        is sorted.
        I can treat the matrix as a one dimension sorted array basing on the property of
        the matrix. Then I want to use two pointers to search for the target.
        Binary search method will give me a time complexity of O(log(mn)). The space complexity
        is O(1).
        """
        if not matrix or not matrix[0]:
            return False
        m = len(matrix)
        n = len(matrix[0])
        end = m * n - 1
        start = 0
        # check if target is smaller than the smallest value or larger than the
        # largest value
        if matrix[0][0] > target:
            return False
        if matrix[m - 1][n - 1] < target:
            return False
        while start + 1 < end:
            mid = start + (end - start) / 2
            row = mid / n
            col = mid % n
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                end = mid
            else:
                start = mid
        if matrix[start /
                  n][start %
                     n] == target or matrix[end /
                                            n][end %
                                               n] == target:
            return True
        else:
            return False

    def searchMatrix2(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool

        This function produces whether the matrix contains target. Basing on the property of
        of the matrix. I will start from the left down corner and do a step-wise search for
        target. The time complexity is O(n) and the space complexity is O(1).
        """
        if not matrix or not matrix[0]:
            return False
        m = len(matrix)
        n = len(matrix[0])
        # start from left down side
        row = m - 1
        col = 0
        while row >= 0 and col < n:
            print matrix[row][col]
            # check to step right or up
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                row -= 1
            else:
                col += 1
        return False

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        This function returns the first bad version. To find the first one, I will
        use two pointers, (start=0, end=n-1). Check if mid is a bad version. If so,
        the right half of the versions can be ignored and if mid is a good version, the left half
        of the versions can be ignored.
        The time complexity is O(logn) and the space complexity is O(1)
        """
        if n == 0:
            return 0
        start = 1
        end = n
        while start + 1 < end:
            mid = start + (end - start) / 2
            if isBadVersion(mid):
                end = mid
            else:
                start = mid
        if isBadVersion(start):
            return start
        else:
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

    def test_searchMatrix(self):
        self.assertEqual(case.searchMatrix(
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]], 8), True)
        self.assertEqual(case.searchMatrix(
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]], 10), False)
        self.assertEqual(case.searchMatrix(
            [[1, 2, 6], [7, 9, 11], [13, 15, 19]], 8), False)

    def test_searchMatrix2(self):
        self.assertEqual(case.searchMatrix(
            [[1, 2, 3], [2, 3, 4], [3, 4, 5]], 1), True)
        self.assertEqual(case.searchMatrix(
            [[1, 2, 3], [2, 3, 4], [3, 4, 5]], 6), False)
        self.assertEqual(case.searchMatrix([[]], 6), False)

if __name__ == "__main__":
    unittest.main()
