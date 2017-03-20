"""
108. Convert Sorted Array to Binary Search Tree Add to List
DescriptionSubmissionsSolutions
Total Accepted: 112377
Total Submissions: 273666
Difficulty: Easy
Contributors: Admin
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

Hide Company Tags Airbnb
Hide Tags Tree Depth-first Search
Hide Similar Problems (M) Convert Sorted List to Binary Search Tree

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        elif len(nums) == 1:
            return TreeNode(nums[0])
        else:
            mid = len(nums) // 2
            node = TreeNode(nums[mid])
            node.left = self.sortedArrayToBST(nums[0:mid])
            node.right = self.sortedArrayToBST(nums[mid + 1:len(nums)])
        return node
