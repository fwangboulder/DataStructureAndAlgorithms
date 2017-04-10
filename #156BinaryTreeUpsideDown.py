"""
156. Binary Tree Upside Down Add to List
DescriptionSubmissionsSolutions
Total Accepted: 22443
Total Submissions: 51620
Difficulty: Medium
Contributors: Admin
Given a binary tree where all the right nodes are either leaf nodes with a sibling (a left node that shares the same parent node) or empty, flip it upside down and turn it into a tree where the original right nodes turned into left leaf nodes. Return the new root.

For example:
Given a binary tree {1,2,3,4,5},
    1
   / \
  2   3
 / \
4   5
return the root of the binary tree [4,5,2,#,#,3,1].
   4
  / \
 5   2
    / \
   3   1
confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.

Hide Company Tags LinkedIn
Hide Tags Tree
Hide Similar Problems (E) Reverse Linked List

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        stack = []
        # append left nodes to stack
        while root is not None:
            stack.append(root)
            root = root.left
        # initialize new root
        new_root = stack.pop()
        runner = new_root
        while len(stack) != 0:
            # pop off parent node, need to clear left and right for cyclical
            # case
            parent = stack.pop()
            parent.left = None
            runner.right = parent
            runner.left = parent.right
            # clear right after, becauses we needed to use it to set
            # runner.left
            parent.right = None
            runner = runner.right
        return new_root
