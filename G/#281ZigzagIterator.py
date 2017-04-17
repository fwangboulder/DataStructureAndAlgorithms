"""
281. Zigzag Iterator Add to List
DescriptionHintsSubmissionsSolutions
Total Accepted: 24242
Total Submissions: 48956
Difficulty: Medium
Contributor: LeetCode
Given two 1d vectors, implement an iterator to return their elements alternately.

For example, given two 1d vectors:

v1 = [1, 2]
v2 = [3, 4, 5, 6]
By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1, 3, 2, 4, 5, 6].

Follow up: What if you are given k 1d vectors? How well can your code be extended to such cases?

Clarification for the follow up question - Update (2015-09-18):
The "Zigzag" order is not clearly defined and is ambiguous for k > 2 cases. If "Zigzag" does not look right to you, replace "Zigzag" with "Cyclic". For example, given the following input:

[1,2,3]
[4,5,6,7]
[8,9]
It should return [1,4,8,2,5,9,3,6,7].
Hide Company Tags Google
Hide Tags Design
Hide Similar Problems (M) Binary Search Tree Iterator (M) Flatten 2D Vector (M) Peeking Iterator (M) Flatten Nested List Iterator

"""
class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.q=collections.deque([x[::-1] for x in [v1,v2] if x])


    def next(self):
        """
        :rtype: int
        """
        tmp=self.q.popleft()
        cur=tmp.pop()
        if tmp:
            self.q.append(tmp)
        return cur



    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.q)!=0


# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
