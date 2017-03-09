"""
89. Gray Code Add to List
Description  Submission  Solutions
Total Accepted: 81502
Total Submissions: 205142
Difficulty: Medium
Contributors: Admin
The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

00 - 0
01 - 1
11 - 3
10 - 2
Note:
For a given n, a gray code sequence is not uniquely defined.

For example, [0,2,3,1] is also a valid gray code sequence according to the above definition.

For now, the judge is able to judge based on one instance of gray code sequence. Sorry about that.

Hide Company Tags Amazon
Hide Tags Backtracking

"""


class Solution(object):

    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        return self.back(n)

    def back(self, n):
        if n == 1:
            return [0, 1]
        cur = []
        pre = self.back(n - 1)
        for x in xrange(len(pre) - 1, -1, -1):
            cur.append(2**(n - 1) + pre[x])
        return pre + cur
