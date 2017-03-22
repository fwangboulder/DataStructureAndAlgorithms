"""
118. Pascal's Triangle Add to List
DescriptionSubmissionsSolutions
Total Accepted: 121083
Total Submissions: 323894
Difficulty: Easy
Contributors: Admin
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
Hide Company Tags Apple Twitter
Hide Tags Array
Hide Similar Problems (E) Pascal's Triangle II

"""


class Solution(object):

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        if numRows == 0:
            return res

        res.append([1])

        for i in range(2, numRows + 1):
            tmp = [1] * i
            prev = res[-1]
            for j in range(1, i - 1):
                tmp[j] = prev[j - 1] + prev[j]
            res.append(tmp)
        return res
