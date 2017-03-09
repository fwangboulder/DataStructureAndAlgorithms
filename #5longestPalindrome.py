"""
5. Longest Palindromic Substring   Add to List QuestionEditorial Solution  My Submissions
Total Accepted: 166828
Total Submissions: 676384
Difficulty: Medium
Contributors: Admin
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.
Example:

Input: "cbbd"

Output: "bb"
Hide Company Tags Amazon Microsoft Bloomberg
Hide Tags String
Hide Similar Problems (H) Shortest Palindrome (E) Palindrome Permutation (H) Palindrome Pairs

"""


class Solution(object):

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''
        for i in xrange(len(s)):

            tmp = self.help(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            tmp = self.help(s, i, i + 1)
            if len(tmp) > len(res):
                res = tmp
        return res

    def help(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r]
