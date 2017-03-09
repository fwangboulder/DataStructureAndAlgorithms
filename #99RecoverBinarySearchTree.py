"""
99. Recover Binary Search Tree Add to List
Description  Submission  Solutions
Total Accepted: 67782
Total Submissions: 233777
Difficulty: Hard
Contributors: Admin
Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Note:
A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?
Hide Tags Tree Depth-first Search

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """

        it = self.isValidBST(root)
        a, b = next(it)
        c = next(it, None)
        if c:
            _, c = c
            a.val, c.val = c.val, a.val
        else:
            a.val, b.val = b.val, a.val

    def isValidBST(self, root):
        pre, cur, stack = None, root, []
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            s = stack.pop()
            if pre and s.val <= pre.val:
                yield pre, s
            pre, cur = s, s.right
