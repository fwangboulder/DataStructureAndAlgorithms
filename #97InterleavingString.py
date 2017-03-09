"""
97. Interleaving String Add to List
Description  Submission  Solutions
Total Accepted: 64775
Total Submissions: 268978
Difficulty: Hard
Contributors: Admin
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.

Hide Tags Dynamic Programming String

Keep two points on s1 and s2 and traverse s3, the current char in s3 is
either from s1 or s2 or both. Use a set to record all possibility and dp on.

The key here is to use a set to record the pointers, because duplicates
are possible, using a list cause TLE.

"""


class Solution(object):

    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        l1, l2 = len(s1), len(s2)
        if l1 + l2 != len(s3):
            return False

        last = set([(0, 0)])
        for char in s3:
            current = set()
            for i, j in last:
                if i < l1 and s1[i] == char:
                    current.add((i + 1, j))
                if j < l2 and s2[j] == char:
                    current.add((i, j + 1))
            if not current:
                return False
            last = current
        return True
