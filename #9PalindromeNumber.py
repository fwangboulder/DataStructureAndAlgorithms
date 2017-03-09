"""
9. Palindrome Number   Add to List QuestionEditorial Solution  My Submissions
Total Accepted: 177669
Total Submissions: 519559
Difficulty: Easy
Contributors: Admin
Determine whether an integer is a palindrome. Do this without extra space.

click to show spoilers.

Hide Tags Math
Hide Similar Problems (E) Palindrome Linked List

"""


class Solution(object):

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        tmp = x
        hfactor = 1
        while tmp:
            hfactor *= 10
            tmp /= 10
        hfactor /= 10
        while x:
            if x % 10 == x / hfactor:
                x = x % hfactor
                x /= 10

            else:
                return False
            hfactor /= 100
        return True
