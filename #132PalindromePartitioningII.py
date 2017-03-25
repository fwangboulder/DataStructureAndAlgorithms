"""
DescriptionSubmissionsSolutions
Total Accepted: 66095
Total Submissions: 279123
Difficulty: Hard
Contributors: Admin
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.

Hide Tags Dynamic Programming
Hide Similar Problems (M) Palindrome Partitioning

"""


class Solution(object):

    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        DP
        We parameterize the problem with index k which answers the question: How many min-cuts are required to cut the string s[k:]?
        min_cut(k) = min(min_cut(j))+1 such that s[k:j] is a palindrome
        min_cut(k) = 0 if s[k:] is a palindrome
        """
        cache_dp = {}
        return self.helper(0, s, self.is_palindrome(s), cache_dp)

    def is_palindrome(self, s):
        N = len(s)
        cache = [[False] * N for _ in range(N)]
        for i in range(N):
            cache[i][i] = True
            if i + 1 < N:
                cache[i][i + 1] = (s[i] == s[i + 1])
        # Incrementally build with increasing lengths from 3 to final
        for length in range(3, len(s) + 1):
            j = length - 1
            for i in range(N):
                if i + j < N:
                    cache[i][i + j] = cache[i + 1][i + \
                        j - 1] and (s[i] == s[i + j])
        return cache

    def helper(self, k, s, cache, cache_dp):
        if k in cache_dp:
            return cache_dp[k]
        else:
            cache_dp[k] = float('inf')
            for i in range(k, len(s)):
                if cache[k][i]:
                    cache_dp[k] = 0 if i == len(
                        s) - 1 else min(cache_dp[k], self.helper(i + 1, s, cache, cache_dp) + 1)
            return cache_dp[k]
