"""
50. Pow(x, n)   Add to List QuestionEditorial Solution  My Submissions
Total Accepted: 131271
Total Submissions: 486613
Difficulty: Medium
Contributors: Admin
Implement pow(x, n).

Hide Company Tags LinkedIn Google Bloomberg Facebook
Hide Tags Binary Search Math
Hide Similar Problems (E) Sqrt(x) (M) Super Pow

"""


class Solution(object):

    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1

        if n < 0:
            n = -n
            x = 1 / x
        ans = 1
        while n > 0:
            if n & 1:
                ans *= x
            x *= x
            n >>= 1

        return ans
