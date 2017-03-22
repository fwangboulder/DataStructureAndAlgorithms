"""
119. Pascal's Triangle II Add to List
DescriptionSubmissionsSolutions
Total Accepted: 106964
Total Submissions: 299854
Difficulty: Easy
Contributors: Admin
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?

Hide Company Tags Amazon
Hide Tags Array
Hide Similar Problems (E) Pascal's Triangle

"""


class Solution(object):

    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = []

        res.append(1)
        if rowIndex == 0:
            return res

        res.append(1)
        if rowIndex == 1:
            return res
        for i in range(2, rowIndex + 1):
            tmp = [1] * (i + 1)
            for j in range(1, i):
                tmp[j] = res[j - 1] + res[j]
            res = tmp
        return res
