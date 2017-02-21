"""
92. Reverse Linked List II Add to List
Description  Submission  Solutions
Total Accepted: 98720
Total Submissions: 329560
Difficulty: Medium
Contributors: Admin
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.

Hide Tags Linked List
Hide Similar Problems (E) Reverse Linked List

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy=ListNode(0)
        dummy.next=head
        prev=dummy
        for i in range(m-1):
            prev=prev.next
        cur=prev.next
        rev=None
        for i in range(n-m+1):
            tmp=cur.next
            cur.next=rev
            rev=cur
            cur=tmp
        prev.next.next=cur
        prev.next=rev
        return dummy.next
