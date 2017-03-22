"""
115. Distinct Subsequences Add to List
DescriptionSubmissionsSolutions
Total Accepted: 66231
Total Submissions: 214296
Difficulty: Hard
Contributors: Admin
Given a string S and a string T, count the number of distinct subsequences of T in S.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Here is an example:
S = "rabbbit", T = "rabbit"

Return 3.

Hide Tags Dynamic Programming String
Have you met this question in a real interview? Yes

From here we can easily fill the whole grid: for each (x, y), we check if S[x] == T[y] we add the previous item and the previous item in the previous row, otherwise we copy the previous item in the same row. The reason is simple:

if the current character in S doesn't equal to current character T, then we have the same number of distinct subsequences as we had without the new character.
if the current character in S equal to the current character T, then the distinct number of subsequences: the number we had before plus the distinct number of subsequences we had with less longer T and less longer S.
An example:
S: [acdabefbc] and T: [ab]

first we check with a:
           *  *
      S = [acdabefbc]
mem[1] = [0111222222]

then we check with ab:

               *  * ]
      S = [acdabefbc]
mem[1] = [0111222222]
mem[2] = [0000022244]
And the result is 4, as the distinct subsequences are:

      S = [a   b    ]
      S = [a      b ]
      S = [   ab    ]
      S = [   a   b ]
"""


class Solution(object):

    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m = len(t)
        n = len(s)
        mem = [[0 for _ in xrange(n + 1)] for _ in xrange(m + 1)]

        for i in xrange(n):
            mem[0][i] = 1
        for i in xrange(len(t)):
            for j in xrange(len(s)):
                if s[j] == t[i]:
                    mem[i + 1][j + 1] = mem[i][j] + mem[i + 1][j]
                else:
                    mem[i + 1][j + 1] = mem[i + 1][j]
        return mem[m][n]
