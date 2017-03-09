"""
82. Remove Duplicates from Sorted List II Add to List
Description  Submission  Solutions
Total Accepted: 98005
Total Submissions: 340490
Difficulty: Medium
Contributors: Admin
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.

Hide Tags Linked List

"""
# make sure each cycle one duplicate has been removed
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
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        while head and head.next:
            if head.val == head.next.val:
                head = head.next
                while head and head.next and head.val == head.next.val:
                    head = head.next
                head = head.next
                pre.next = head
            else:
                pre = head
                head = head.next

        return dummy.next


# second create a dummy
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
        dummy = ListNode(0)
        pre = dummy
        dummy.next = head
        while head and head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                pre = pre.next
                head = head.next
        return dummy.next
