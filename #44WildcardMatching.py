"""
44. Wildcard Matching   Add to List QuestionEditorial Solution  My Submissions
Total Accepted: 81616
Total Submissions: 426603
Difficulty: Hard
Contributors: Admin
Implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "*") → true
isMatch("aa", "a*") → true
isMatch("ab", "?*") → true
isMatch("aab", "c*a*b") → false
Hide Company Tags Google Snapchat Two Sigma Facebook Twitter
Hide Tags Dynamic Programming Backtracking Greedy String
Hide Similar Problems (H) Regular Expression Matching
"""

lass Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        dp[0][0] = True
        #s is empty
        for i in range(1, len(p) + 1):
            if p[i - 1] == '*':
                # match 0
                dp[0][i] = dp[0][i - 1]
            else:
                break

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if s[
                    i -
                    1] == p[
                    j -
                    1] or p[
                    j -
                        1] == '?':  # match or one of them is '?'
                    dp[i][j] = dp[i - 1][j - 1]
                # match 0 s[i-1]=p[j-2]; match 1 s[i-1]=p[j-1];consume s[i-1]
                # and rematch s[i-2]=p[j-1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 1] | dp[i - 1][j - 1] | dp[i - 1][j]

                else:
                    dp[i][j] = False

        return dp[len(s)][len(p)]
