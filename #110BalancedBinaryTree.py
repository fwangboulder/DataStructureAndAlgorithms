"""
110. Balanced Binary Tree Add to List
DescriptionSubmissionsSolutions
Total Accepted: 161156
Total Submissions: 439984
Difficulty: Easy
Contributors: Admin
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Hide Company Tags Bloomberg
Hide Tags Tree Depth-first Search
Hide Similar Problems (E) Maximum Depth of Binary Tree

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def height(node):
            if not node:
                return 0

            return max(height(node.left), height(node.right)) + 1
        if not root:
            return True

        if abs(height(root.left) - height(root.right)) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        return False
