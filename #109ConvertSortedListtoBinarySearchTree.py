"""
109. Convert Sorted List to Binary Search Tree Add to List
DescriptionSubmissionsSolutions
Total Accepted: 98188
Total Submissions: 296213
Difficulty: Medium
Contributors: Admin
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

Hide Company Tags Zenefits
Hide Tags Depth-first Search Linked List
Hide Similar Problems (E) Convert Sorted Array to Binary Search Tree

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """

    def sortedListToBST(self, head):
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)

        dummyHead = ListNode(0)
        dummyHead.next = head
        slow, fast = dummyHead, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        root = TreeNode(slow.next.val)
        root.right = self.sortedListToBST(slow.next.next)
        slow.next = None
        root.left = self.sortedListToBST(head)

        return root
