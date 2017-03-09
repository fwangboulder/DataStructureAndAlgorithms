"""
14. Longest Common Prefix   Add to List QuestionEditorial Solution  My Submissions
Total Accepted: 146233
Total Submissions: 477558
Difficulty: Easy
Contributors: Admin
Write a function to find the longest common prefix string amongst an array of strings.

Hide Company Tags Yelp
Hide Tags String

"""


class Solution(object):

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        shortest = min(strs, key=len)
        for i, val in enumerate(shortest):
            for s in strs:
                if s[i] != val:
                    return shortest[:i]
        return shortest
