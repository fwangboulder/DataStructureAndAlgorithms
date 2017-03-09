"""
76. Minimum Window Substring
Description  Submission  Solutions  Add to List
Total Accepted: 88790
Total Submissions: 369286
Difficulty: Hard
Contributors: Admin
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the empty string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.

Hide Company Tags LinkedIn Snapchat Uber Facebook
Hide Tags Hash Table Two Pointers String
Hide Similar Problems (H) Substring with Concatenation of All Words (M) Minimum Size Subarray Sum (H) Sliding Window Maximum

Store t in a hashtable. with count as the length of this hashtable
start=0 as the start position
for loop: s.
while count==0:
    resLen=i-start+1
"""


class Solution(object):

    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        count = 0
        m = {}
        for c in t:
            if c not in m:
                count += 1
                m[c] = 0
            m[c] += 1

        start = 0
        size = len(s)
        ansLen = size + 1
        ans = ''
        for end in xrange(size):
            if s[end] not in m:
                continue
            m[s[end]] -= 1
            if m[s[end]] == 0:
                count -= 1
            while count == 0:
                print m, ans
                if end - start + 1 < ansLen:
                    ansLen = end - start + 1
                    ans = s[start:end + 1]
                startC = s[start]
                start += 1
                print startC, start
                if startC not in m:
                    continue
                m[startC] += 1
                if m[startC] == 1:
                    count += 1
                    break

        if ansLen == size + 1:
            return ''
        return ans
