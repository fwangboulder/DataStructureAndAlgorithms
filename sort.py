#! /usr/bin/env python

#####################
### by Fang Wang  ###
### March 17, 2017###
#####################

import unittest

"""
partition array
Given an array nums of integers and an int k, partition the array (i.e move the elements in "nums") such that:

All elements < k are moved to the left
All elements >= k are moved to the right
Return the partitioning index, i.e the first index i nums[i] >= k.


"""


class Solution(object):
    """
    @param nums: The integer array you should partition
    @param k: As description
    @return: The index after partition
    """

    def partitionArray(self, nums, k):
        start, end = 0, len(nums) - 1
        while start <= end:
            while start <= end and nums[start] < k:
                start += 1
            while start <= end and nums[end] >= k:
                end -= 1
            if start <= end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        return start

    def mergeSort(self, alist):
        """
        :type alist: List[int]
        :rtype: List[int]
        this function returns the sorted order of alist.
        Using a divide and conquer strategy as a way to improve the performance
        of sorting algorithms. The first algorithm we will study is the merge sort.
         Merge sort is a recursive algorithm that continually splits a list in half.
         If the list is empty or has one item, it is sorted by definition (the base case).
         If the list has more than one item, we split the list and recursively invoke a
         merge sort on both halves. Once the two halves are sorted, the fundamental
         operation, called a merge, is performed. The time complexity is O(nlogn)
         and the space complexity is O(n).
        """
        if len(alist) > 1:
            # split the list into two parts, sort each part
            mid = len(alist) // 2
            lefthalf = alist[:mid]
            righthalf = alist[mid:]
            self.mergeSort(lefthalf)
            self.mergeSort(righthalf)
            i = 0
            j = 0
            k = 0
            # merge left and right half
            while i < len(lefthalf) and j < len(righthalf):
                if lefthalf[i] < righthalf[j]:
                    alist[k] = lefthalf[i]
                    i += 1
                else:
                    alist[k] = righthalf[j]
                    j += 1
                k += 1
            # if lefthalf still has element
            while i < len(lefthalf):
                alist[k] = lefthalf[i]
                i += 1
                k += 1
            # if righthalf still has element
            while j < len(righthalf):
                alist[k] = righthalf[j]
                j += 1
                k += 1
        return alist
#######################quick Sort#####################

    def quickSort(self, alist):
        """
        :type alist: List[int]
        :rtype: List[int]
        The quick sort uses divide and conquer to gain the same advantages as
        the merge sort, while not using additional storage.
        A quick sort first selects a value, which is called the pivot value.
         Although there are many different ways to choose the pivot value,
         we will simply use the first item in the list. The role of the pivot
         value is to assist with splitting the list. The actual position where
         the pivot value belongs in the final sorted list, commonly called the
         split point, will be used to divide the list for subsequent calls to
         the quick sort. The average time complexity is O(nlogn) and the space
         complexity is O(1).
        """
        self.quickSortHelper(alist, 0, len(alist) - 1)
        return alist

    def quickSortHelper(self, alist, first, last):
        if first < last:
            splitpoint = self.partition(alist, first, last)
            self.quickSortHelper(alist, first, splitpoint - 1)
            self.quickSortHelper(alist, splitpoint + 1, last)

    def partition(self, alist, first, last):
        # pick the pivotvalue as the first value
        pivotvalue = alist[first]
        leftindex = first + 1
        rightindex = last
        done = 0
        while not done:
            # leftindex increase
            while leftindex <= rightindex and alist[leftindex] <= pivotvalue:
                leftindex += 1
            # rightindex decrease
            while alist[rightindex] >= pivotvalue and rightindex >= leftindex:
                rightindex -= 1
            # cross, then break the while loop
            if rightindex < leftindex:
                done = 1
            # not cross, left and right value swap
            else:
                tmp = alist[leftindex]
                alist[leftindex] = alist[rightindex]
                alist[rightindex] = tmp

        # after all the partition is done, swap the first value with the
        # rightindex
        tmp = alist[first]
        alist[first] = alist[rightindex]
        alist[rightindex] = tmp
        return rightindex

# test
testCase = Solution()


class test(unittest.TestCase):

    def test_mergeSort(self):
        self.assertEqual(testCase.mergeSort([5, 4, 26, 93, 17, 77, 31, 44, 55, 20]), [
                         4, 5, 17, 20, 26, 31, 44, 55, 77, 93])

    def test_quickSort(self):
        self.assertEqual(testCase.quickSort([5, 4, 26, 93, 17, 77, 31, 44, 55, 20]), [
                         4, 5, 17, 20, 26, 31, 44, 55, 77, 93])

    def test_partitionArray(self):
        self.assertEqual(testCase.partitionArray(
            [5, 4, 26, 93, 17, 77, 31, 44, 55, 20], 26), 4)
if __name__ == "__main__":
    unittest.main()
