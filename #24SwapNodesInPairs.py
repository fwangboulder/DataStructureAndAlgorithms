"""
24. Swap Nodes in Pairs   Add to List QuestionEditorial Solution  My Submissions
Total Accepted: 143390
Total Submissions: 385887
Difficulty: Easy
Contributors: Admin
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.

Hide Company Tags Microsoft Bloomberg Uber
Hide Tags Linked List
Hide Similar Problems (H) Reverse Nodes in k-Group

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        pre = dummy = ListNode(0)
        dummy.next = head.next
        while head and head.next:
            pre.next = head.next
            q = head.next
            head.next = q.next
            q.next = head
            pre = head
            head = head.next
        return dummy.next
