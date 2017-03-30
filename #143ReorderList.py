"""
143. Reorder List Add to List
DescriptionSubmissionsSolutions
Total Accepted: 86699
Total Submissions: 347632
Difficulty: Medium
Contributors: Admin
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.

Hide Tags Linked List

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        # There are at least three nodes
        if not head or not head.next or not head.next.next:
            return
        # two pointers
        slow, fast = head, head

        while fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next
        # Find the first node and the middle node
        head1, head2 = head, slow.next
        slow.next, cur, pre = None, head2, None
        # reverse the second half
        while cur:
            curnext = cur.next
            cur.next = pre
            pre = cur
            cur = curnext
        cur1, cur2 = head1, pre
        while cur2:
            next1, next2 = cur1.next, cur2.next
            cur1.next = cur2
            cur2.next = next1
            cur1, cur2 = next1, next2
