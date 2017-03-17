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

    def tranversePre(self, root, res):
        if not root:
            return
        res.append(root.val)
        self.tranversePre(root.left, res)
        self.tranversePre(root.right, res)

    def tranverseIn(self, root, res):
        if not root:
            return
        self.tranverseIn(root.left, res)
        res.append(root.val)
        self.tranverseIn(root.right, res)

    def tranversePost(self, root, res):
        if not root:
            return
        self.tranversePost(root.left, res)
        self.tranversePost(root.right, res)
        res.append(root.val)

    def preorderTraversalRecursion(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]

        time complexity O(n) and space complexity O(n).
        """
        res = []
        self.tranversePre(root, res)
        return res

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]

        time complexity O(n) and space complexity O(n).
        """
        if root is None:
            return []
        # divide
        left = self.preorderTraversal(root.left)
        right = self.preorderTraversal(root.right)

        # conquer
        return [root.val] + left + right

    def preorderTraversalStack(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]

        1) Create an empty stack nodeStack and push root node to stack.
        2) Do following while nodeStack is not empty.
            a) Pop an item from stack and print it.
            b) Push right child of popped item to stack
            c) Push left child of popped item to stack

        """
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
        this function return the inorder transversal of a tree.

        """
        if root is None:
            return []

        # divide
        left = self.inorderTraversal(root.left)
        right = self.inorderTraversal(root.right)

        # conquer
        return left + [root.val] + right

    def inorderTraversalStack(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        this function return the inorder transversal of a tree.

        1) Create an empty stack S.
        2) Initialize current node as root
        3) Push the current node to S and set current = current->left until current is NULL
        4) If current is NULL and stack is not empty then
            a) Pop the top item from stack.
            b) Print the popped item, set current = popped_item->right
            c) Go to step 3.
        5) If current is NULL and stack is empty then we are done.
        """
        if not root:
            return []
        stack = []
        inorder = []
        current = root
        done = 0
        while not done:
            if current:
                stack.append(current)
                current = current.left
            else:
                if stack:
                    current = stack.pop()
                    inorder.append(current.val)
                    current = current.right
                else:
                    done = 1

        return inorder

    def inorderTraversalRecursion(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]

        time complexity O(n) and space complexity O(n).
        """
        res = []
        self.tranverseIn(root, res)
        return res

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        # divide
        left = self.postorderTraversal(root.left)
        right = self.postorderTraversal(root.right)

        # conquer
        return left + right + [root.val]

    def postorderTraversalStack(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]

        1.1 Create an empty stack
        2.1 Do following while root is not NULL
            a) Push root's right child and then root to stack.
            b) Set root as root's left child.
        2.2 Pop an item from stack and set it as root.
            a) If the popped item has a right child and the right child
                is at top of stack, then remove the right child from stack,
                push the root back and set root as root's right child.
            b) Else print root's data and set root as NULL.
       2.3 Repeat steps 2.1 and 2.2 while stack is not empty.
        """
        def peek(stack):
            if len(stack) > 0:
                return stack[-1]
            return None
        # Check for empty tree
        if not root:
            return []
        done = 0
        stack = []
        postorder = []
        current = root
        while not done:
            while current:
                # Push root's right child and then root to stack
                if current.right:
                    stack.append(current.right)
                stack.append(current)
                # set current as current's left child
                current = current.left
            # Pop an item from stack and set it as current.
            current = stack.pop()
            # if the popped item has a right child
            # and the right child is not processed yet, then make sure the
            # right child is processed before the root
            if current.right and peek(stack) == current.right:
                stack.pop()  # remove the right child
                stack.append(current)  # push current back to the stack
                current = current.right
            else:
                postorder.append(current.val)
                current = None
            if not stack:
                break
        return postorder

    def postorderTraversalRecursion(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]

        time complexity O(n) and space complexity O(n).
        """
        res = []
        self.tranversePost(root, res)
        return res

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

    def test_inorderTraversalStack(self):
        self.assertEqual(
            tree.inorderTraversalStack(root), [
                1, 2, 3, 4, 6, 7, 8])

    def test_inorderTraversalRecursion(self):
        self.assertEqual(
            tree.inorderTraversalRecursion(root), [
                1, 2, 3, 4, 6, 7, 8])

    def test_preorderTraversal(self):
        self.assertEqual(tree.preorderTraversal(root), [1, 2, 3, 4, 7, 6, 8])

    def test_preorderTraversalStack(self):
        self.assertEqual(
            tree.preorderTraversalStack(root), [
                1, 2, 3, 4, 7, 6, 8])

    def test_preorderTraversalRecursion(self):
        self.assertEqual(
            tree.preorderTraversalRecursion(root), [
                1, 2, 3, 4, 7, 6, 8])

    def test_postorderTraversal(self):
        self.assertEqual(tree.postorderTraversal(root), [6, 8, 7, 4, 3, 2, 1])

    def test_postorderTraversalStack(self):
        self.assertEqual(
            tree.postorderTraversalStack(root), [
                6, 8, 7, 4, 3, 2, 1])

    def test_postorderTraversalRecursion(self):
        self.assertEqual(
            tree.postorderTraversalRecursion(root), [
                6, 8, 7, 4, 3, 2, 1])


if __name__ == "__main__":
    unittest.main()
