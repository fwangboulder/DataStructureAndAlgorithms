"""
23. Merge k Sorted Lists   Add to List QuestionEditorial Solution  My Submissions
Total Accepted: 126202
Total Submissions: 485015
Difficulty: Hard
Contributors: Admin
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Hide Company Tags LinkedIn Google Uber Airbnb Facebook Twitter Amazon Microsoft
Hide Tags Divide and Conquer Linked List Heap
Hide Similar Problems (E) Merge Two Sorted Lists (M) Ugly Number II

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

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

    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        tmp = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tmp.next = l1
                l1 = l1.next
            else:
                tmp.next = l2
                l2 = l2.next
            tmp = tmp.next
        if l1:
            tmp.next = l1
        elif l2:
            tmp.next = l2
        return dummy.next
