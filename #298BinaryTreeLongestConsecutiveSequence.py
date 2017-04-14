"""
298. Binary Tree Longest Consecutive Sequence Add to List
DescriptionHintsSubmissionsSolutions
Total Accepted: 26871
Total Submissions: 66476
Difficulty: Medium
Contributor: LeetCode
Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).

For example,
   1
    \
     3
    / \
   2   4
        \
         5
Longest consecutive sequence path is 3-4-5, so return 3.
   2
    \
     3
    /
   2
  /
 1
Longest consecutive sequence path is 2-3,not3-2-1, so return 2.
Hide Company Tags Google
Hide Tags Tree
Hide Similar Problems (H) Longest Consecutive Sequence (M) Binary Tree Longest Consecutive Sequence II

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        stack=[(root,1)]
        res=0

        while stack:
            node, length=stack.pop()
            res=max(res,length)
            for i in [node.left, node.right]:
                if i:
                    if i.val==node.val+1:
                        l=length+1
                    else:
                        l=1
                    stack.append((i,l))
        return res
            
