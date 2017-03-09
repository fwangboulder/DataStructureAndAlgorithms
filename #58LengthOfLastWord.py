"""
58. Length of Last Word   Add to List QuestionEditorial Solution  My Submissions
Total Accepted: 128044
Total Submissions: 410898
Difficulty: Easy
Contributors: Admin
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example,
Given s = "Hello World",
return 5.

Hide Tags String
"""


class Solution(object):

    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip().split()
        if not s:
            return 0
        return len(s[-1])
