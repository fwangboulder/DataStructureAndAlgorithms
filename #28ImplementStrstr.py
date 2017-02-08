"""
28. Implement strStr()   Add to List QuestionEditorial Solution  My Submissions
Total Accepted: 154188
Total Submissions: 570082
Difficulty: Easy
Contributors: Admin
Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Hide Company Tags Pocket Gems Microsoft Apple Facebook
Hide Tags Two Pointers String
Hide Similar Problems (H) Shortest Palindrome (E) Repeated Substring Pattern

"""
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        if needle =='':
            return 0
        if needle in haystack:
            return len(haystack.split(needle)[0])
        return -1
        
