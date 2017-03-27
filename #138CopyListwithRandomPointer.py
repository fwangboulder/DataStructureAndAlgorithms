"""
138. Copy List with Random Pointer Add to List
DescriptionSubmissionsSolutions
Total Accepted: 102869
Total Submissions: 387681
Difficulty: Medium
Contributors: Admin
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

Hide Company Tags Amazon Microsoft Bloomberg Uber
Hide Tags Hash Table Linked List
Hide Similar Problems (M) Clone Graph

"""

# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None


class Solution(object):

    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        dic = dict()
        if not head:
            return None
        node = head
        # store node in dictionary
        dic[head] = RandomListNode(head.label)
        while node:
            if node.next:
                if node.next not in dic:
                    # store the node.next value as a randomlistnode type
                    dic[node.next] = RandomListNode(node.next.label)
                dic[node].next = dic[node.next]
            if node.random:
                if node.random not in dic:
                    dic[node.random] = RandomListNode(node.random.label)
                dic[node].random = dic[node.random]
            node = node.next
        return dic[head]
