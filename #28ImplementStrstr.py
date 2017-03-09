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
        This function returns the first index of the target string in source string.
        The edge condition: 1)if needle is empty, return 0; 2) if needle not existed,
        return -1.
        Normal condtion: Loop haystack and check if it equals to the target string.
        This method has a time complexity of O(mn) and a space complexity of O(1).
        If I use python split function, the code will become really easy. 
        """

        if needle == '':
            return 0
        if needle in haystack:
            return len(haystack.split(needle)[0])
        return -1
