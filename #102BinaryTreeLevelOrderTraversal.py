"""
102. Binary Tree Level Order Traversal Add to List
DescriptionSubmissionsSolutions
Total Accepted: 158612
Total Submissions: 417413
Difficulty: Medium
Contributors: Admin
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
Hide Company Tags LinkedIn Facebook Amazon Microsoft Apple Bloomberg
Hide Tags Tree Breadth-first Search
Hide Similar Problems (M) Binary Tree Zigzag Level Order Traversal (E) Binary Tree Level Order Traversal II (E) Minimum Depth of Binary Tree (M) Binary Tree Vertical Order Traversal
Have you met this question in a real interview? Yes  No

"""
from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res=[]
        tmp=[]
        d=deque()
        d.append(root)
        while d:
            for i in xrange(len(d)):
                node=d.popleft()
                tmp.append(node.val)
                if node.left:
                    d.append(node.left)
                if node.right:
                    d.append(node.right)
            res+=[tmp]
            tmp=[]
        return res
                
