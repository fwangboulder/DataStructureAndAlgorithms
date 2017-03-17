#! /usr/bin/env python
import unittest

"""
Binary Tree Preorder Traversal(#144)

Given a binary tree, return the preorder traversal of its node's value.

Binary Tree Inorder Traversal(#94)
Given a binary tree, return the inorder traversal of its node's value.

"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Tree(object):

    def createNode(self,x):
        # use this function to create a node
        return TreeNode(x)

    def insert(self, node, x):
        #Insert a node into the tree
        if not node:
            return self.createNode(x)
        if x<node.val:
            node.left=self.insert(node.left, x)
        elif x>node.val:
            node.right=self.insert(node.right,x)
        return node



    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        return [root.val] + self.preorderTraversal(root.left) \
                          + self.preorderTraversal(root.right)



    def preorderTraversalStack(self,root):
        if not root:
            return []
        stack=[root]
        preorder=[]
        while stack:
            node=stack.pop()
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
        if root == None:
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
        return self.postorderTraversal(root.left)+self.postorderTraversal(root.right) \
                +[root.val]

def main():
    root = None
    tree = Tree()
    root = tree.insert(root, 10)
    # print root
    tree.insert(root, 20)
    tree.insert(root, 30)
    tree.insert(root, 40)
    tree.insert(root, 70)
    tree.insert(root, 60)
    tree.insert(root, 80)

    print "Traverse Inorder"
    print tree.inorderTraversal(root)

    print "Traverse Preorder"
    print tree.preorderTraversal(root)
    print "Traverse Preorder Stack method"
    print tree.preorderTraversalStack(root)
    print "Traverse Postorder"
    print tree.postorderTraversal(root)




if __name__ == "__main__":
    main()
