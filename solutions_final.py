#! /usr/bin/env python
import unittest
################################################################
# Question 1


def question1(s, t):
    """
    :type s: str
    :type t: str
    :rtype: boolean
    This function check whether any anagram of t is a substring for s.
    """
    m = len(s)
    n = len(t)
    # edge conditions
    if n == 0:
        return True
    if n > m:
        return False
    # store t in dictionary dt
    dt = dict()
    for c in t:
        dt[c] = dt.get(c, 0) + 1

    # loop s
    for i in range(m):
        ds = {}

        for j in range(i, i + n):
            # this subS!=dt case, break
            if s[j] not in dt:
                break
            # store each subS in dictionary ds
            else:
                ds[s[j]] = ds.get(s[j], 0) + 1
        # ds==dt means one anagram of t is the substring of s, return True
        if ds == dt:
            return True
    # not found ds==dt in the loop
    return False
# test


class TestQ1(unittest.TestCase):

    def test_Q11(self):
        self.assertEqual(question1('udacity', 'ad'), True)

    def test_Q12(self):
        self.assertEqual(question1('a', 'ab'), False)

    def test_Q13(self):
        self.assertEqual(question1('a', ''), True)


################################################################
# Question 2


def question2(a):
    # a helper function to count the palindrome length centered at the current
    # position
    """
    :type a: str
    :rtype: str
    This function returns the longest palindromic string in a.
    """
    def helper(a, l, r):
        while l >= 0 and r < len(a) and a[l] == a[r]:
            l -= 1
            r += 1
        return a[l + 1:r]
    res = ''

    for i in xrange(len(a)):
        # odd case, like "aba"
        tmp = helper(a, i, i)
        if len(tmp) > len(res):
            res = tmp
        # even case, like "abba"
        tmp = helper(a, i, i + 1)
        if len(tmp) > len(res):
            res = tmp
    return res
# test


class TestQ2(unittest.TestCase):

    def test_Q21(self):
        self.assertEqual(question2('abacde'), 'aba')

    def test_Q22(self):
        self.assertEqual(question2('gabbacde'), 'abba')

    def test_Q23(self):
        self.assertEqual(question2('a'), 'a')

################################################################
# Question 3

from collections import defaultdict
from heapq import *


def question3(G):
    """
    :type: dict
    :rtype: dict
    This function generates the minimum weight spanning tree.
    """
    # reformat G and stored it in default dict conn
    conn = defaultdict(list)
    # default dict mst is used to store the res
    mst = defaultdict(list)
    # store all nodes in a list named nodes
    nodes = []
    if not G:
        return {}

    for n1 in G:
        nodes.append(n1)
        for n2, c in G[n1]:
            conn[n1].append((c, n1, n2))
    # select one node and store it in used.Used is a set to store the used node
    used = set(nodes[0])
    # used_edges is a list to store usable edges
    usable_edges = conn[nodes[0]][:]
    # heapify the usable edges
    heapify(usable_edges)

    while usable_edges:
        # while the usable edges is not empty, a heappop will pop out the
        # minimum cost value between two nodes
        c, n1, n2 = heappop(usable_edges)
        # if n2 has not been used before, add it to used set, store it is mst
        # and add new usable edges conn[n2] to usable_edges
        if n2 not in used:
            used.add(n2)
            mst[n1].append((n2, c))
            mst[n2].append((n1, c))
            for v in conn[n2]:
                if v[2] not in used:
                    heappush(usable_edges, v)
    mst = dict(mst)
    return mst
# test
G1 = {'A': [('B', 2)],
      'B': [('A', 2), ('C', 5)],
      'C': [('B', 5)]}
G2 = {'A': [('B', 7), ('D', 5)],
      'B': [('A', 2), ('C', 8), ('D', 9), ('E', 7)],
      'C': [('B', 5), ('E', 5)],
      'D': [('A', 5), ('B', 9), ('E', 15), ('F', 6)],
      'E': [('B', 7), ('C', 5), ('D', 15), ('F', 8), ('G', 9)],
      'F': [('E', 8), ('G', 11)],
      'G': [('E', 9), ('F', 11)]}

G3 = {}


class TestQ3(unittest.TestCase):

    def test_Q31(self):
        self.assertEqual(
            question3(G1), {
                'A': [('B', 2)],
                'C': [('B', 5)],
                'B': [('A', 2), ('C', 5)]})

    def test_Q32(self):
        self.assertEqual(
            question3(G2), {
                'A': [('D', 5), ('B', 7)],
                'C': [('E', 5)],
                'B': [('A', 7), ('E', 7)],
                'E': [('B', 7), ('C', 5), ('G', 9)],
                'D': [('A', 5), ('F', 6)],
                'G': [('E', 9)],
                'F': [('D', 6)]})

    def test_Q33(self):
        self.assertEqual(question3(G3), {})

################################################################
# Question 4


def get_right_node(tree, r):
    branch = tree[r]
    right_node = (len(branch) - 1) - branch[::-1].index(1)
    return right_node


def get_left_node(tree, r):
    branch = tree[r]
    left_node = branch.index(1)
    return left_node


def question4(T, r, n1, n2):
    """
    :type T: List[List[int]]
    :type r: int
    :type n1: int
    :type n2: int
    :rtype: int
    This function returns the lowest common ancestor for n1 and n2.
    """

    if n1 <= len(T) and n2 <= len(T):
        while not (n1 <= r and n2 >= r or
                   n1 >= r and n2 <= r):
            # check if both n1 and n1 less than root, traverse through left
            # subtree
            if n1 < r and n2 < r:
                r = get_left_node(T, r)
            # check if both n1 and n1 greater than root, traverse through right
            # subtree
            elif n1 > r and n2 > r:
                r = get_right_node(T, r)
        # if r is not None return r
        if r is not None:
            return r
    else:
        return None
    ###Method 2###
    # The following method has a time complexity O(n) and space complexity O(V).
    # # ancestors list
    # ancestors = [n1, n2]
    # # current ancestor for n1 and n2
    # n1_ancestor = n1
    # n2_ancestor = n2
    # # found res
    # res = False
    # # while not found
    # while not res:
    #     # loop T
    #     for i, node in enumerate(T):
    #         # There is always one common ancestor, root
    #         if not n1_ancestor == r:
    #             # check if node i is n1's ancestor
    #             if node[n1_ancestor] == 1:
    #                 n1_ancestor = i
    #                 # if node i has already existed in ancestor, res found
    #                 if i in ancestors:
    #                     res = True
    #                     return i
    #                 # if not existed, add it to ancestors list
    #                 ancestors.append(i)
    #         if not n2_ancestor == r:
    #             # check if node i is n2's ancestor
    #             if node[n2_ancestor] == 1:
    #                 n2_ancestor = i
    #                 # if node i has already existed in ancestor, res found
    #                 if i in ancestors:
    #                     res = True
    #                     return i
    #                 # if not existed, add it to ancestors list
    #                 ancestors.append(i)
# test


class TestQ4(unittest.TestCase):

    def test_Q41(self):
        self.assertEqual(question4([[0, 1, 0, 0, 0],
                                    [0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0],
                                    [1, 0, 0, 0, 1],
                                    [0, 0, 0, 0, 0]],
                                   3,
                                   0,
                                   1), 0)

    def test_Q42(self):
        self.assertEqual(question4([[0, 1, 0, 0, 0],
                                    [0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0],
                                    [1, 0, 0, 0, 1],
                                    [0, 0, 0, 0, 0]],
                                   3,
                                   1,
                                   4), 3)

    def test_Q43(self):
        self.assertEqual(question4([[0, 1, 1, 0, 0],
                                    [0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0],
                                    [1, 0, 0, 0, 1],
                                    [0, 0, 0, 0, 0]],
                                   3,
                                   1,
                                   2), 0)

######################################################
# Question 5


class Node():
    # initialize the node obeject

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():
    # Function to initialize head and tail

    def __init__(self):
        self.head = None
        self.tail = None

    def AddNode(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node

        if self.tail is not None:
            self.tail.next = new_node

        self.tail = new_node

    # Find the mth node from the end

    def question5(self, m):
        """
        :type m: int
        :rtype: num
        This functions returns the data of the mth node from the end.
        """
        cur = self.head
        length = 0
        # get the length of the ll
        while cur:
            cur = cur.next
            length += 1
        # The mth node from the end is nth node from the head
        if length < m or m < 1:
            return None
        n = length - m
        cur = self.head
        while n > 0:
            cur = cur.next
            n -= 1
        return cur.data
# Test
lst = LinkedList()
lst.AddNode(1)
lst.AddNode(2)
lst.AddNode(3)
lst.AddNode(4)
lst.AddNode(5)


class TestQ5(unittest.TestCase):

    def test_Q51(self):
        self.assertEqual(lst.question5(4), 2)

    def test_Q52(self):
        self.assertEqual(lst.question5(6), None)

    def test_Q53(self):
        self.assertEqual(lst.question5(1), 5)

    def test_Q54(self):
        self.assertEqual(lst.question5(0), None)
if __name__ == "__main__":
    unittest.main()

# # TechnicalInterviewPractice
# Technical Interview Practice
# 
# # Question 1
# Given two strings s and t, determine whether some anagram of t is a substring of s. For example: if s = "udacity" and t = "ad", then the function returns True. Your function definition should look like: question1(s, t) and return a boolean True or False.
#
# # Question 2
# Given a string a, find the longest palindromic substring contained in a. Your function definition should look like question2(a), and return a string.
#
# # Question 3
# Given an undirected graph G, find the minimum spanning tree within G. A minimum spanning tree connects all vertices in a graph with the smallest possible total weight of edges. Your function should take in and return an adjacency list structured like this:
#
# {'A': [('B', 2)],
#  'B': [('A', 2), ('C', 5)],
#  'C': [('B', 5)]}
# Vertices are represented as unique strings.
#
# # Question 4
# Find the least common ancestor between two nodes on a binary search tree. The least common ancestor is the farthest node from the root that is an ancestor of both nodes. For example, the root is a common ancestor of all nodes on the tree, but if both nodes are descendents of the root's left child, then that left child might be the lowest common ancestor. You can assume that both nodes are in the tree, and the tree itself adheres to all BST properties. The function definition should look like question4(T, r, n1, n2), where T is the tree represented as a matrix, where the index of the list is equal to the integer stored in that node and a 1 represents a child node, r is a non - negative integer representing the root, and n1 and n2 are non - negative integers representing the two nodes in no particular order. For example, one test case might be
#
# question4([[0, 1, 0, 0, 0],
#            [0, 0, 0, 0, 0],
#            [0, 0, 0, 0, 0],
#            [1, 0, 0, 0, 1],
#            [0, 0, 0, 0, 0]],
#           3,
#           1,
#           4)
# and the answer would be 3.
#
# # Question 5
# Find the element in a singly linked list that's m elements from the end. For example, if a linked list has 5 elements, the 3rd element from the end is the 3rd element. The function definition should look like question5(ll, m), where ll is the first node of a linked list and m is the "mth number from the end". You should copy / paste the Node class below to use as a representation of a node in the linked list. Return the value of the node at that position.
#
# ********************************************************************************************************************
#
# Q1 Explanation:
#
# This question is to find out whether some anagram of t is substring of s.
# There are two edge condition:
# 1) t is empty, return True;
# 2)the length of t is bigger that the length of s, return False.
#
# Normal condition:
#
# First, I will store t in a dictionary dt with the key: value as character:total_Count.
# The time complexity for this step is O(n).
#
# To check whether some anagram of t is a substring s, I will loop s to check whether
# subS, whose index starts from i (0= < i <= m - n, m is the length of s) and ends
# at i + n - 1 (n is the length of t) is one of anagram of t. If it exists, return True.
# Else, return False. Then the problem become: how to determine whether two strings (t and subS)
# with the same length are anagram strings to each other. I will store each subS to dictionary ds
# and check if ds == dt. If so, return True. If there is no ds == dt, this means t is not a
# substring of s. This step the time complexity is O(mn).
# My solution for this question has a time complexity of O(mn) and a space complexity of O(m+n).
#
# Q2 Explanation:
#
# To determine the longest palindromic substring contained in variable a, we need to understand
# what is palindromic string first. Palindromic string is a reversed string equals to the string itself.
# Having two pointers moving forward and backward can determine where is the edge of the palindrom.
# Do a loop for the string a. For each character, I will use a helper function to check the
# longest palindromic substring centered at current character. There are two possible situations:
# 'aba' centered at b or 'abba' centered at b. The two pointers move forward and backward respectively until
# they are not equal or they reach the end. If the new substring has a longer length than previous one, update the result.
# The time complexity is O(n ^ 2) and the space complexity is O(1).
#
# Q3 Explanation:
#
# To find the minimum spanning tree, I choose to use prim algorithm in the following steps:
# 1. Picked one node, add this node to a set used and add all possible edges connected to this node to a usable_edges list.
# 2. Find the minimum weight connected to the nodes in the used set. Check if the node connected is already used. If not, add it to the used set, add all possible edges connected to the usable_edges list and stored the connection between two nodes to the result. Repeat this step until there is no usable_edges, then return the result.
#
# In step 2, I need to find minimum weight again and again. Use a heap structure will save time. It is better to reformat the input dictionary value as (weight, node1, node2) format. By applying a heapify function to usable_edges, heappop will always give the minimum weight together with two connected nodes, and heappush will always keep the usable_edges keep the heap structure. The time complexity is O(Elong(V)), where V is the number of nodes and E is the number of edges. The space complexity is O(V).
#
# Q4 Explanation:
# The first method has made the best use of binary search tree property: the root is smaller than
# all children in the left tree and bigger than all the children in the right tree. A recursion Method
# has been used if both n1 and n2 is in the left subtree  or in the right subtree, else return the root.
# The time complexity is O(logV) and the time complexity is O(1).
# For method 2 (I have set it as comments):
# T is the tree represented as a matrix, where the index of the list is equal to the integer stored in that node and a 1 represents a child node. This means once we found node[n] == 1, this mode is the ancestor of n. First, I create an ancestor list with starting value n1, n2. Then I loop T to check whether node[n1] == 1, node[n2] == 1, respectively. If so, check if this node index has already been stored in ancestor list. If existed, return the index. If not existed, add the node index to ancestor list.
# The time complexity is O(n) and the space complexity is O(V), where V is the number of nodes..
#
# Q5 Explanation:
#
# This is a simple linked list problem. Get the data for a node.  First, get the length of the linked list and calculate the target node index. The time complexity is O(n) and the space complexity is O(1) .
#
