"""
3. Longest Substring Without Repeating Characters   Add to List QuestionEditorial Solution  My Submissions
Total Accepted: 237674
Total Submissions: 1002030
Difficulty: Medium
Contributors: Admin
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

Hide Company Tags Amazon Adobe Bloomberg Yelp
Hide Tags Hash Table Two Pointers String
Hide Similar Problems (H) Longest Substring with At Most Two Distinct Characters
"""


class Solution(object):

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = dict()
        start = 0
        maxl = 0
        for i, num in enumerate(s):
            if num in d and start <= d[num]:
                start = d[num] + 1
            else:
                maxl = max(maxl, i - start + 1)
            d[num] = i
        return maxl
