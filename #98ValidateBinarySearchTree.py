"""
98. Validate Binary Search Tree Add to List
Description  Submission  Solutions
Total Accepted: 143738
Total Submissions: 636378
Difficulty: Medium
Contributors: Admin
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:
    2
   / \
  1   3
Binary tree [2,1,3], return true.
Example 2:
    1
   / \
  2   3
Binary tree [1,2,3], return false.
Hide Company Tags Amazon Microsoft Bloomberg Facebook
Hide Tags Tree Depth-first Search
Hide Similar Problems (M) Binary Tree Inorder Traversal (E) Find Mode in Binary Search Tree

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        output = []
        self.inOrder(root, output)

        for i in range(1, len(output)):
            if output[i - 1] >= output[i]:
                return False

        return True

    def inOrder(self, root, output):
        if root is None:
            return

        self.inOrder(root.left, output)
        output.append(root.val)
        self.inOrder(root.right, output)
