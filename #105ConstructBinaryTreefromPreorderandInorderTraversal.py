"""
105. Construct Binary Tree from Preorder and Inorder Traversal Add to List
DescriptionSubmissionsSolutions
Total Accepted: 92961
Total Submissions: 297735
Difficulty: Medium
Contributors: Admin
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

Hide Company Tags Bloomberg
Hide Tags Tree Array Depth-first Search
Hide Similar Problems (M) Construct Binary Tree from Inorder and Postorder Traversal
Have you met this question in a real interview? Yes

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            root = TreeNode(preorder[0])
            root_index = inorder.index(preorder[0])
            preorder.pop(0)
            l_len = len(inorder[:root_index])
            root.left = self.buildTree(preorder, inorder[0:l_len])
            root.right = self.buildTree(preorder, inorder[l_len+1:])
            return root
