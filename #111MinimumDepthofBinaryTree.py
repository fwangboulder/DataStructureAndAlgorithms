"""
111. Minimum Depth of Binary Tree Add to List
DescriptionSubmissionsSolutions
Total Accepted: 154518
Total Submissions: 474030
Difficulty: Easy
Contributors: Admin
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Hide Tags Tree Depth-first Search Breadth-first Search
Hide Similar Problems (M) Binary Tree Level Order Traversal (E) Maximum Depth of Binary Tree

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution(object):

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0
        depth = 1
        l = []
        q = deque([[root, depth]])
        while q:
            front, d = q.popleft()
            if front.left is None and front.right is None:
                l.append(d)
            if front.left:
                q += [[front.left, d + 1]]
            if front.right:
                q += [[front.right, d + 1]]
        return min(l)

# method 2
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        depth = 1
        l = []

        def dfs(root, depth):
            if root.left is None and root.right is None:
                l.append(depth)
            if root.left:
                dfs(root.left, depth + 1)
            if root.right:
                dfs(root.right, depth + 1)
        dfs(root, depth)
        return min(l)
