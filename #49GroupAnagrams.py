"""
49. Group Anagrams   Add to List QuestionEditorial Solution  My Submissions
Total Accepted: 113347
Total Submissions: 352543
Difficulty: Medium
Contributors: Admin
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note: All inputs will be in lower-case.

Hide Company Tags Amazon Bloomberg Uber Facebook Yelp
Hide Tags Hash Table String
Hide Similar Problems (E) Valid Anagram (M) Group Shifted Strings
"""


class Solution(object):

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for s in strs:
            lst = sorted(s)
            lst = tuple(lst)
            if lst in d:
                d[lst].append(s)
            else:
                d[lst] = [s]
        res = []
        for i in d.values():
            res.append(i)
        return res
