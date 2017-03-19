#! /usr/bin/env python
#############################
###by Fang Wang #############
###March 19 2017########
###########################

import unittest
"""
270. Closest Binary Search Tree Value   Add to List QuestionEditorial Solution  My Submissions
Total Accepted: 27396
Total Submissions: 71642
Difficulty: Easy
Contributors: Admin
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:
Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
Hide Company Tags Microsoft Google Snapchat
Hide Tags Tree Binary Search
Hide Similar Problems (M) Count Complete Tree Nodes (H) Closest Binary Search Tree Value II

"""


class Solution(object):

    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        This function returns the value in the binary search tree that is closest to
        the target. Use the recursion method. The time complexity is O(logn) and
        the space compexity is O(1).
        """
        if not root:
            return None
        #use a helper function to return the res and diff between target and res
        result, diff = self.ClosestValueHelper(root, target)
        return result

    def ClosestValueHelper(self, root, target):

        result = root.val
        diff = abs(root.val - target)
        #target is larger than root.val, go right
        if target >= root.val:
            if root.right:
                rightResult, rightDiff = self.ClosestValueHelper(root.right, target)
                if diff > rightDiff:
                    result = rightResult
                    diff = rightDiff
        #if target is smaller than root.val, go left
        else:
            if root.left:
                leftResult, leftDiff = self.ClosestValueHelper(root.left, target)
                if diff > leftDiff:
                    result = leftResult
                    diff = leftDiff
        return result, diff
