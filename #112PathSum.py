"""
112. Path Sum Add to List
DescriptionSubmissionsSolutions
Total Accepted: 150394
Total Submissions: 451196
Difficulty: Easy
Contributors: Admin
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

Hide Company Tags Microsoft
Hide Tags Tree Depth-first Search
Hide Similar Problems (M) Path Sum II (H) Binary Tree Maximum Path Sum (M) Sum Root to Leaf Numbers (E) Path Sum III

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        elif root.left is None and root.right is None:
            return sum - root.val == 0
        return self.hasPathSum(
            root.left,
            sum -
            root.val) or self.hasPathSum(
            root.right,
            sum -
            root.val)
