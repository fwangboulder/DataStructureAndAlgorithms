"""
69. Sqrt(x)   Add to List QuestionEditorial Solution  My Submissions
Total Accepted: 130743
Total Submissions: 483660
Difficulty: Easy
Contributors: Admin
Implement int sqrt(int x).

Compute and return the square root of x.

Hide Company Tags Bloomberg Apple Facebook
Hide Tags Binary Search Math
Hide Similar Problems (M) Pow(x, n) (E) Valid Perfect Square

"""
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        start=0
        end=x
        while start+1<end:
            mid=start+(end-start)/2
            if mid*mid>x:
                end=mid
            elif (mid+1)*(mid+1)<x:
                start=mid
            elif mid*mid==x:
                return mid
            elif (mid+1)*(mid+1)==x:
                return mid+1
            else:
                return mid
        if start*start==x:
            return start
        elif end*end==x:
            return end
