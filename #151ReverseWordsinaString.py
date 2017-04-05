"""
151. Reverse Words in a String Add to List
DescriptionSubmissionsSolutions
Total Accepted: 147434
Total Submissions: 937599
Difficulty: Medium
Contributors: Admin
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Update (2015-02-12):
For C programmers: Try to solve it in-place in O(1) space.

click to show clarification.

Hide Company Tags Microsoft Snapchat Apple Bloomberg Yelp
Hide Tags String
Hide Similar Problems (M) Reverse Words in a String II

"""


class Solution(object):

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split()
        end = len(s) - 1
        start = 0
        while start <= end:
            tmp = s[start]
            s[start] = s[end]
            s[end] = tmp
            start += 1
            end -= 1
        return ' '.join(s)
