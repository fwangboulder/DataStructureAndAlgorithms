"""
4. Median of Two Sorted Arrays   Add to List QuestionEditorial Solution  My Submissions
Total Accepted: 139853
Total Submissions: 670649
Difficulty: Hard
Contributors: Admin
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
Hide Company Tags Google Zenefits Microsoft Apple Yahoo Dropbox Adobe
Hide Tags Binary Search Array Divide and Conquer

"""


class Solution(object):

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l = len(nums1) + len(nums2)
        if l % 2 == 1:
            return self.findKth(nums1, nums2, l // 2)
        else:
            return (self.findKth(nums1, nums2, l // 2) +
                    self.findKth(nums1, nums2, l // 2 - 1)) / 2.0

    def findKth(self, A, B, k):
        if len(A) > len(B):
            A, B = B, A
        if not A:
            return B[k]
        if k == len(A) + len(B) - 1:
            return max(A[-1], B[-1])
        i = len(A) // 2
        j = k - i
        if A[i] > B[j]:
            return self.findKth(A[:i], B[j:], i)
        else:
            return self.findKth(A[i:], B[:j], j)
