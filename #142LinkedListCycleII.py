"""
142. Linked List Cycle II Add to List
DescriptionSubmissionsSolutions
Total Accepted: 106611
Total Submissions: 343617
Difficulty: Medium
Contributors: Admin
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.

Follow up:
Can you solve it without using extra space?

Hide Tags Linked List Two Pointers
Hide Similar Problems (E) Linked List Cycle (M) Find the Duplicate Number

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        while not head or not head.next:
            return None
        slow = fast = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            # fast goes two times faster than slow
            # 2s=f
            # when fast==slow, fast goes one more circle comparing with slow
            # then move the slow to the head. and now slow and fast has the same speed to go
            # in the end they will meet at the start node of the loop.
            # draw picture to see why.
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None
