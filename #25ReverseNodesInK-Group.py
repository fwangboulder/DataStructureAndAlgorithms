"""
25. Reverse Nodes in k-Group   Add to List QuestionEditorial Solution  My Submissions
Total Accepted: 80863
Total Submissions: 271351
Difficulty: Hard
Contributors: Admin
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Hide Company Tags Microsoft Facebook
Hide Tags Linked List
Hide Similar Problems (E) Swap Nodes in Pairs

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not self.check(head,k):
            return head

        dummy=ListNode(0)
        pre=dummy
        while self.check(head,k):
            tmp=head
            rev=None
            for i in xrange(k):
                q=head.next
                head.next=rev
                rev=head
                head=q
            pre.next=rev
            tmp.next=head
            pre=tmp
        return dummy.next

    def check(self,head,k):
        tmp=head
        while k and tmp:
            k-=1
            tmp=tmp.next
        return k==0
