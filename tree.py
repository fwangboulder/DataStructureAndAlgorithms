#! /usr/bin/env python

# By Fang Wang
# March 2017
import unittest

"""
Binary Tree Preorder Traversal(#144)

Given a binary tree, return the preorder traversal of its node's value.

Binary Tree Inorder Traversal(#94)
Given a binary tree, return the inorder traversal of its node's value.

Binary Tree Postorder Traversal(#145)
Given a binary tree, return the inorder traversal of its node's value.

"""
# Definition for a binary tree node.


class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Tree(object):

    def createNode(self, x):
        # use this function to create a node
        return TreeNode(x)

    def insert(self, node, x):
        # Insert a node into the tree
        if not node:
            return self.createNode(x)
        if x < node.val:
            node.left = self.insert(node.left, x)
        elif x > node.val:
            node.right = self.insert(node.right, x)
        return node

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        return [root.val] + self.preorderTraversal(root.left) \
                          + self.preorderTraversal(root.right)

    def preorderTraversalStack(self, root):
        if not root:
            return []
        stack = [root]
        preorder = []
        while stack:
            node = stack.pop()
            preorder.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return preorder

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        return self.inorderTraversal(root.left) + [root.val] \
            + self.inorderTraversal(root.right)

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        return self.postorderTraversal(
            root.left) + self.postorderTraversal(root.right) + [root.val]

# create a tree.

root = None
tree = Tree()
root = tree.insert(root, 1)
# print root
tree.insert(root, 2)
tree.insert(root, 3)
tree.insert(root, 4)
tree.insert(root, 7)
tree.insert(root, 6)
tree.insert(root, 8)

print "Traverse Inorder"
print tree.inorderTraversal(root)

print "Traverse Preorder"
print tree.preorderTraversal(root)
print "Traverse Preorder Stack method"
print tree.preorderTraversalStack(root)
print "Traverse Postorder"
print tree.postorderTraversal(root)

# test


class testTree(unittest.TestCase):

    def test_inorderTraversal(self):
        self.assertEqual(tree.inorderTraversal(root), [1, 2, 3, 4, 6, 7, 8])

    def test_preorderTraversal(self):
        self.assertEqual(tree.preorderTraversal(root), [1, 2, 3, 4, 7, 6, 8])

    def test_preorderTraversalStack(self):
        self.assertEqual(
            tree.preorderTraversalStack(root), [
                1, 2, 3, 4, 7, 6, 8])

    def test_postorderTraversal(self):
        self.assertEqual(tree.postorderTraversal(root), [6, 8, 7, 4, 3, 2, 1])


if __name__ == "__main__":
    unittest.main()
