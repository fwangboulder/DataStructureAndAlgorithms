"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

Hide Company Tags Amazon Microsoft Bloomberg Airbnb Adobe
Hide Tags Linked List Math
Hide Similar Problems (M) Multiply Strings (E) Add Binary (E) Sum of Two Integers (E) Add Strings (M) Add Two Numbers II
Total Accepted: 233815
Total Submissions: 887479
Difficulty: Medium
Contributors: Admin
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry=0
        n=head=ListNode(0)
        while l1 or l2 or carry:
            v=0
            if l1:
                v+=l1.val
                l1=l1.next
            if l2:
                v+=l2.val
                l2=l2.next
            if carry:
                v+=carry
            carry=v/10
            v%=10
            #print v
            n.next=ListNode(v)
            n=n.next
        return head.next
