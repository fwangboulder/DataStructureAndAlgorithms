"""
148. Sort List Add to List
DescriptionSubmissionsSolutions
Total Accepted: 97714
Total Submissions: 351309
Difficulty: Medium
Contributors: Admin
Sort a linked list in O(n log n) time using constant space complexity.

Hide Tags Linked List Sort
Hide Similar Problems (E) Merge Two Sorted Lists (M) Sort Colors (M) Insertion Sort List

"""
    Definition for singly - linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# merge sort


class Solution(object):

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:  # check whether head  is empty
            return None
        if not head.next:  # check whether it has only one node
            return head
        # set three pointer (fast and slow and previous) starting from the head
        pre, slow, fast = None, head, head
        while fast and fast.next:   # fast goes to the end, slow to the middle, pre is mid-1
            pre, slow, fast = slow, slow.next, fast.next.next

        pre.next = None   # break the pre.next

        # do not understand? DFS?constant space complexity
        left, right = self.sortList(head), self.sortList(slow)
        pre_head = cur = ListNode(None)  # set pre_head as current and none
        while left and right:  # while loop for left and right
            if left.val < right.val:  # compare left and right value
                cur.next, left.next, left = left, None, left.next  # cur.next=smaller,
            else:
                cur.next, right.next, right = right, None, right.next
            cur = cur.next  # go the the next value
        if left or right:  # if there are more left or right value,
            cur.next = left or right

        return pre_head.next
