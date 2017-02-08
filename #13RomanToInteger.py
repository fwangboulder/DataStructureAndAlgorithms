"""
13. Roman to Integer   Add to List QuestionEditorial Solution  My Submissions
Total Accepted: 125590
Total Submissions: 287632
Difficulty: Easy
Contributors: Admin
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.

Hide Company Tags Microsoft Bloomberg Uber Facebook Yahoo
Hide Tags Math String
Hide Similar Problems (M) Integer to Roman
"""

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        res=0
        if not s:
            return res
        l=len(s)
        d={'I':1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        for i in xrange(l-1):
            if d[s[i]]<d[s[i+1]]:
                res-=d[s[i]]
            else:
                res+=d[s[i]]
        return res+d[s[-1]]
