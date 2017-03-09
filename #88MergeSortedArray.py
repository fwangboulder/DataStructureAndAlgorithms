"""
88. Merge Sorted Array Add to List
Description  Submission  Solutions
Total Accepted: 145499
Total Submissions: 461437
Difficulty: Easy
Contributors: Admin
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.

Hide Company Tags Microsoft Bloomberg Facebook
Hide Tags Array Two Pointers
Hide Similar Problems (E) Merge Two Sorted Lists

"""


class Solution(object):

    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        start = m + n - 1
        m = m - 1
        n = n - 1

        while start:
            if nums1[m] > nums2[n] and m >= 0 and n >= 0:
                nums1[start] = nums1[m]
                m -= 1
                start -= 1
            elif nums1[m] <= nums2[n] and m >= 0 and n >= 0:
                nums1[start] = nums2[n]
                n -= 1
                start -= 1
            if n < 0:
                break
            if m < 0:
                nums1[:n + 1] = nums2[:n + 1]
                break
        if start == 0 and n == 0:
            nums1[start] = nums2[n]
