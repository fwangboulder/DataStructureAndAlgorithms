"""
129. Sum Root to Leaf Numbers Add to List
DescriptionSubmissionsSolutions
Total Accepted: 103920
Total Submissions: 291556
Difficulty: Medium
Contributors: Admin
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.

Hide Tags Tree Depth-first Search
Hide Similar Problems (E) Path Sum (H) Binary Tree Maximum Path Sum

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def __init__(self):
        self.total = 0

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        dfs
        """
        self.sumNumbersHelper(root, 0)
        return self.total

    def sumNumbersHelper(self, root, res):

        if not root:
            return
        res = res * 10 + root.val
        if not root.left and not root.right:
            self.total += res
            return
        self.sumNumbersHelper(root.left, res)
        self.sumNumbersHelper(root.right, res)
