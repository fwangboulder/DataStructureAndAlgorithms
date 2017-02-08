"""
10. Regular Expression Matching   Add to List QuestionEditorial Solution  My Submissions
Total Accepted: 117453
Total Submissions: 497433
Difficulty: Hard
Contributors: Admin
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
Hide Company Tags Google Uber Airbnb Facebook Twitter
Hide Tags Dynamic Programming Backtracking String
Hide Similar Problems (H) Wildcard Matching

"""

###dp
"""
dp[i][j] means s[0:i-1] match p[0:j-1]

p[j-1] not "." and "*": dp[i][j]=dp[i-1][j-1] and s[i-1]==p[j-1]
p[j-1] is '.': dp[i][j]=dp[i-1][j-1]

p[j-1] is '*':
       match 0 (delete p[j-2]) then p[0:j-1]=p[0:j-3]
        dp[i][j]=dp[i][j-2]
       mathch 1  then p[0:j-1]=p[0:j-2]
       dp[i][j]=dp[i][j-1]

       match multiple elements: then p[0:j-1]=p[0:j]
"""
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[False for i in range(0,len(p) + 1)] for j in range(0, len(s) + 1)]
        #empty s and empty p
        dp[0][0] = True
        #print dp

        #s is empty string
        for i in range(1, len(p) + 1):
            if (p[i - 1] == '*'):
                dp[0][i] = dp[0][i - 2]
        #print dp
        # s is not empty
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                #
                if p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2] #match 0: s[i-1]=p[j-3]
                    if s[i - 1] == p[j - 2] or p[j - 2] == '.': #match 1 s[i-1]=p[j-2]
                                                                #match 2 s[i-2]=p[j-1]   s: aa p:a*
                        dp[i][j] |= dp[i-1][j]
                else:
                    if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                        dp[i][j] = dp[i - 1][j - 1]
        return dp[len(s)][len(p)]
