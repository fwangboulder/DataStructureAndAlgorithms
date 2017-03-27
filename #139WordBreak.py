"""
139. Word Break Add to List
DescriptionSubmissionsSolutions
Total Accepted: 135389
Total Submissions: 467881
Difficulty: Medium
Contributors: Admin
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. You may assume the dictionary does not contain duplicate words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".

UPDATE (2017/1/4):
The wordDict parameter had been changed to a list of strings (instead of a set of strings). Please reload the code definition to get the latest changes.

Hide Company Tags Google Uber Facebook Amazon Yahoo Bloomberg Pocket Gems
Hide Tags Dynamic Programming
Hide Similar Problems (H) Word Break II

"""


class Solution(object):

    def wordBreak(self, s, words):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        d = [False] * len(s)
        for i in range(len(s)):
            for w in words:
                if w == s[i - len(w) + 1:i + 1] and (d[i - \
                                  len(w)] or i - len(w) == -1):
                    d[i] = True
        return d[-1]
