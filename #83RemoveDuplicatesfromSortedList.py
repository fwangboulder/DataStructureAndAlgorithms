"""
83. Remove Duplicates from Sorted List Add to List
Description  Submission  Solutions
Total Accepted: 163784
Total Submissions: 419218
Difficulty: Easy
Contributors: Admin
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.

Hide Tags Linked List

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        cur = head.next
        prev = head
        while cur:
            if cur.val == prev.val:
                prev.next = cur.next
                cur = cur.next
            else:
                prev = prev.next
                cur = cur.next
        return head
