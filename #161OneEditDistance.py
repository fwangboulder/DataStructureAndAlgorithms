"""
161. One Edit Distance Add to List
DescriptionSubmissionsSolutions
Total Accepted: 29184
Total Submissions: 94690
Difficulty: Medium
Contributors: Admin
Given two strings S and T, determine if they are both one edit distance apart.

Hide Company Tags Snapchat Uber Facebook Twitter
Hide Tags String
Hide Similar Problems (H) Edit Distance

"""
class Solution(object):

    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m = len(s)
        n = len(t)

        diff = abs(m - n)

        if diff > 1:
            return False

        if m < n:
            return self.isOneEditDistance(t, s)

        i = 0
        while i < n and s[i] == t[i]:
            i = i + 1

        if diff == 0:
            i = i + 1

        while i < n and s[i + diff] == t[i]:
            i = i + 1

        return i == n
