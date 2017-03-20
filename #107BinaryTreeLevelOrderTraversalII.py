"""
107. Binary Tree Level Order Traversal II Add to List
DescriptionSubmissionsSolutions
Total Accepted: 118339
Total Submissions: 306063
Difficulty: Easy
Contributors: Admin
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
Hide Tags Tree Breadth-first Search
Hide Similar Problems (M) Binary Tree Level Order Traversal

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution(object):

    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        d = deque()
        d.append(root)
        res, tmp = [], []
        while d:
            for i in xrange(len(d)):
                node = d.popleft()
                tmp.append(node.val)
                if node.left:
                    d.append(node.left)
                if node.right:
                    d.append(node.right)
            res += [tmp]
            tmp = []
        return res[::-1]
