"""
124. Binary Tree Maximum Path Sum Add to List
DescriptionSubmissionsSolutions
Total Accepted: 89844
Total Submissions: 353759
Difficulty: Hard
Contributors: Admin
Given a binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

For example:
Given the below binary tree,

       1
      / \
     2   3
Return 6.

Hide Company Tags Microsoft Baidu
Hide Tags Tree Depth-first Search
Hide Similar Problems (E) Path Sum (M) Sum Root to Leaf Numbers

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int

        Hhelper function returns two values:

        The max sum of all paths ending in the given node (need be extended through the parent)
        The max sum of all paths anywhere in tree rooted at the given node (need not be extended through the parent).
        """

        def maxsums(node):
            if not node:
                return [-2**31] * 2
            left = maxsums(node.left)
            right = maxsums(node.right)
            # print node.val, [node.val + max(left[0], right[0], 0),max(left +
            # right + [node.val + left[0] + right[0]])]
            return [node.val + max(left[0], right[0], 0),
                    max(left + right + [node.val + left[0] + right[0]])]
        return max(maxsums(root))
