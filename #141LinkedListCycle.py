"""
141. Linked List Cycle Add to List
DescriptionSubmissionsSolutions
Total Accepted: 165717
Total Submissions: 465853
Difficulty: Easy
Contributors: Admin
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?

Hide Company Tags Amazon Microsoft Bloomberg Yahoo
Hide Tags Linked List Two Pointers
Hide Similar Problems (M) Linked List Cycle II

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        while not head or not head.next:
            return False
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False
