"""
145. Binary Tree Postorder Traversal Add to List
DescriptionSubmissionsSolutions
Total Accepted: 133322
Total Submissions: 340959
Difficulty: Hard
Contributors: Admin
Given a binary tree, return the postorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [3,2,1].

Note: Recursive solution is trivial, could you do it iteratively?

Hide Tags Tree Stack
Hide Similar Problems (M) Binary Tree Inorder Traversal

"""


class Solution(object):

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        return self.postorderTraversal(
            root.left) + self.postorderTraversal(root.right) + [root.val]
