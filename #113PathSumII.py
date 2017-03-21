"""
113. Path Sum II Add to List
DescriptionSubmissionsSolutions
Total Accepted: 117415
Total Submissions: 364115
Difficulty: Medium
Contributors: Admin
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]
Hide Company Tags Bloomberg
Hide Tags Tree Depth-first Search
Hide Similar Problems (E) Path Sum (E) Binary Tree Paths (E) Path Sum III

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []

        if not root.right and not root.left:
            return [[root.val]] if root.val == sum else []

        return [[root.val] +
                i for i in self.pathSum(root.left, sum -
                                        root.val) +
                self.pathSum(root.right, sum -
                             root.val)]
