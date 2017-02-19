"""
86. Partition List Add to List
Description  Submission  Solutions
Total Accepted: 89496
Total Submissions: 282231
Difficulty: Medium
Contributors: Admin
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.

Hide Tags Linked List Two Pointers

"""
# combine left and right side in the end.
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        left=ListNode(0)
        right=ListNode(0)
        cur1=left
        cur2=right
        while head:
            if head.val<x:
                cur1.next=ListNode(head.val)
                head=head.next
                cur1=cur1.next
            else:
                cur2.next=ListNode(head.val)
                head=head.next
                cur2=cur2.next

        if right.next:
            cur1.next=right.next
        return left.next
