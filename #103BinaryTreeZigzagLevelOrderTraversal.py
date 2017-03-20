"""
103. Binary Tree Zigzag Level Order Traversal Add to List
DescriptionSubmissionsSolutions
Total Accepted: 91708
Total Submissions: 277220
Difficulty: Medium
Contributors: Admin
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
Hide Tags LinkedIn Bloomberg Microsoft
Hide Tags Tree Breadth-first Search Stack
Hide Similar Problems (M) Binary Tree Level Order Traversal
Have you met this question in a real interview? Yes
"""

from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        tmp = []
        d = deque()
        d.append(root)
        level = 0
        flag = 1
        while d:
            for i in xrange(len(d)):
                node = d.popleft()
                tmp.append(node.val)
                if node.left:
                    d.append(node.left)
                if node.right:
                    d.append(node.right)
            res += [tmp[::flag]]
            tmp = []
            flag *= -1
        return res
