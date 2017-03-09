"""
61. Rotate List   Add to List QuestionEditorial Solution  My Submissions
Total Accepted: 94899
Total Submissions: 393992
Difficulty: Medium
Contributors: Admin
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.

Hide Tags Linked List Two Pointers
Hide Similar Problems (E) Rotate Array

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        p = head
        l = 0
        # calculate the length of linklist
        while p:
            l += 1
            p = p.next

        if l < 2 or k % l == 0:
            return head
        q = head
        for _ in range(l - k % l - 1):
            q = q.next
        if not q.next:
            return head
        else:
            newhead = q.next

            q.next = None
            p = newhead
        while p and p.next:
            p = p.next
        p.next = head

        return newhead
