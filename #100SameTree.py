"""
100. Same Tree Add to List
Description  Submission  Solutions
Total Accepted: 184482
Total Submissions: 405176
Difficulty: Easy
Contributors: Admin
Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.

Hide Company Tags Bloomberg
Hide Tags Tree Depth-first Search

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        elif p and q:

            return p.val == q.val and self.isSameTree(
                p.left, q.left) and self.isSameTree(
                p.right, q.right)

        else:
            return False
