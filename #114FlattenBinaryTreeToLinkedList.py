"""
114. Flatten Binary Tree to Linked List Add to List
DescriptionSubmissionsSolutions
Total Accepted: 117124
Total Submissions: 343627
Difficulty: Medium
Contributors: Admin
Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
click to show hints.

Hide Company Tags Microsoft
Hide Tags Tree Depth-first Search


"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        stack = []
        while stack or root:
            if root:
                if root.right:
                    stack.append(root.right)
                if root.left:
                    root.right = root.left
                    root.left = None
                elif stack:
                    root.right = stack.pop()
                root = root.right

    def __init__(self):
        self.prev = None

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.flatten(root.right)
        self.flatten(root.left)

        root.right = self.prev
        root.left = None
        self.prev = root
