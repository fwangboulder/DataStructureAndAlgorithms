"""
7. Reverse Integer   Add to List QuestionEditorial Solution  My Submissions
Total Accepted: 200740
Total Submissions: 847504
Difficulty: Easy
Contributors: Admin
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

click to show spoilers.

Hide Company Tags Bloomberg Apple
Hide Tags Math
Hide Similar Problems (E) String to Integer (atoi)
"""
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        maxint=2**31-1
        flag=1
        if x<0:
            flag=-1
            x=-x
        res=0
        while x:
            res=res*10+x%10
            x=x/10
        if res>maxint:
            return 0
        return res*flag
        
