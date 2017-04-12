"""
160. Intersection of Two Linked Lists Add to List
DescriptionSubmissionsSolutions
Total Accepted: 119512
Total Submissions: 395589
Difficulty: Easy
Contributors: Admin
Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
Credits:
Special thanks to @stellari for adding this problem and creating all test cases.

Hide Company Tags Amazon Microsoft Bloomberg Airbnb
Hide Tags Linked List

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        #start from the same len and compare if the vals are the same
        lenA=lenB=0
        curA=headA
        curB=headB
        if not curA or not curB:
            return None
        while curA:
            lenA+=1
            curA=curA.next
        while curB:
            lenB+=1
            curB=curB.next
        curA=headA
        curB=headB
        if lenA>lenB:
            for i in range(lenA-lenB):
                curA=curA.next
        elif lenB>lenA:
            for i in range(lenB-lenA):
                curB=curB.next
        while curB!=curA:
            curB=curB.next
            curA=curA.next
        return curA
