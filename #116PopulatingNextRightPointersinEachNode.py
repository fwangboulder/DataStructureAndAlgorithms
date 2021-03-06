"""
116. Populating Next Right Pointers in Each Node Add to List
DescriptionSubmissionsSolutions
Total Accepted: 123381
Total Submissions: 334350
Difficulty: Medium
Contributors: Admin
Given a binary tree

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
For example,
Given the following perfect binary tree,
         1
       /  \
      2    3
     / \  / \
    4  5  6  7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL
Hide Company Tags Microsoft
Hide Tags Tree Depth-first Search
Hide Similar Problems (M) Populating Next Right Pointers in Each Node II (M) Binary Tree Right Side View
Have you met this question in a real interview? Yes
"""
# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        while root.left:
            cur = root.left
            prev = None
            while root:
                if prev:
                    prev.next = root.left
                root.left.next = root.right
                prev = root.right
                root = root.next
            root = cur
