"""
12. Integer to Roman   Add to List QuestionEditorial Solution  My Submissions
Total Accepted: 90936
Total Submissions: 211779
Difficulty: Medium
Contributors: Admin
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.

Hide Company Tags Twitter
Hide Tags Math String
Hide Similar Problems (E) Roman to Integer (H) Integer to English Words
"""


class Solution(object):

    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        dic = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
        rv = ""
        i = 1
        while num:
            mod = num % 10
            if mod < 4:
                rv = mod * dic[i] + rv
            elif mod == 4:
                rv = dic[i] + dic[i * 5] + rv
            elif mod == 5:
                rv = dic[i * 5] + rv
            elif mod > 5 and mod < 9:
                rv = dic[i * 5] + (mod - 5) * dic[i] + rv
            elif mod == 9:
                rv = dic[i] + dic[i * 10] + rv
            i = i * 10
            num = num / 10
        return rv
