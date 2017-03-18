#! /usr/bin/env python

# by Fang Wang
# March 17, 2017

import unittest
"""
Leetcode problems

Merge two sorted list (#21)

Add two numbers (#2)

Swap Nodes in Pairs (#24)

Merge K Sorted Linked Lists (#23)

Partition List (#86)
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.

"""

# Definition for singly-linked list.


class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        I insert a dummy head before the new list so I do not have to deal with
        special cases such as initializing the new list's head. Then the new list's
        head could just easily be returned as dummy head's next node.
        """
        # insert a dummy for the new list
        dummy = ListNode(0)
        tmp = dummy
        while l1 and l2:
            # compare l1.val and l2.val, add the smaller one to the new list
            # add l1
            if l1.val < l2.val:
                tmp.next = l1
                l1 = l1.next
            # add l2
            else:
                tmp.next = l2
                l2 = l2.next
            # move tmp
            tmp = tmp.next
        # check if l1 has more nodes
        if l1:
            tmp.next = l1
        # check if l2 has more nodes
        if l2:
            tmp.next = l2
        return dummy.next

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        l = len(lists)
        if l == 0:
            return []
        while l > 1:
            tmp_res = []
            for i in range(0, l, 2):
                if i + 1 < l:

                    tmp_res.append(self.mergeTwoLists(lists[i], lists[i + 1]))
                else:
                    tmp_res.append(lists[i])
            lists = tmp_res
            l = len(lists)
        if l == 1:
            return lists[0]

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Create a dummy head
        dummy = ListNode(0)
        carry = 0
        tmp = dummy
        # add l1.val and l2.val and carry
        while l1 and l2:
            s = l1.val + l2.val + carry
            # val=s%10
            tmp.next = ListNode(s % 10)
            # new carry
            carry = s / 10
            tmp = tmp.next
            l1 = l1.next
            l2 = l2.next
        # check if l1 has more nodes
        while l1:
            s = l1.val + carry
            tmp.next = ListNode(s % 10)
            carry = s / 10
            tmp = tmp.next
            l1 = l1.next
            if not carry:
                tmp.next = l1
                break
        # check if l2 has more nodes
        while l2:
            s = l2.val + carry
            tmp.next = ListNode(s % 10)
            carry = s / 10
            tmp = tmp.next
            l2 = l2.next
            if not carry:
                tmp.next = l2
                break
        # check if carry is 1
        if not l1 and not l2 and carry:
            tmp.next = ListNode(carry)
        return dummy.next

    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # edge condition, only one node or no node
        if not head or not head.next:
            return head
        # create dummy head
        dummy = ListNode(0)
        dummy.next = head
        # previous node
        prev = dummy
        # swap the connections tmp=prev.next.next
        while prev.next and prev.next.next:
            tmp = prev.next.next
            prev.next.next = tmp.next
            tmp.next = prev.next
            prev.next = tmp
            prev = prev.next.next
        return dummy.next

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

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(7)
l1.next.next.next = ListNode(9)
l2 = ListNode(3)
l2.next = ListNode(4)
l2.next.next = ListNode(8)
l3 = ListNode(1)
l3.next = ListNode(2)
l3.next.next = ListNode(3)
l3.next.next.next = ListNode(4)
testCase = Solution()

# test


class test_TestCase(unittest.TestCase):

    def test_mergeTwoLists(self):
        res = []
        node = testCase.mergeTwoLists(l1, l2)
        while node:
            res.append(node.val)
            node = node.next
        self.assertEqual(res, [1, 2, 3, 4, 7, 8, 9])

    def test_addTwoNumbers(self):
        res = []
        node = testCase.addTwoNumbers(l1, l2)
        while node:
            res.append(node.val)
            node = node.next
        self.assertEqual(res, [4, 6, 5, 0, 1])

    def test_swapPairs(self):
        res = []
        node = testCase.swapPairs(l3)
        while node:
            res.append(node.val)
            node = node.next
        self.assertEqual(res, [2, 1, 4, 3])

if __name__ == "__main__":
    unittest.main()
