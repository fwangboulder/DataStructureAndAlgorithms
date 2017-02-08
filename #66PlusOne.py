"""
66. Plus One   Add to List QuestionEditorial Solution  My Submissions
Total Accepted: 147550
Total Submissions: 397739
Difficulty: Easy
Contributors: Admin
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.

Hide Company Tags Google
Hide Tags Array Math
Hide Similar Problems (M) Multiply Strings (E) Add Binary (M) Plus One Linked List

"""
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits:
            return
        n=len(digits)
        i=len(digits)-1
        while i>=0:

            if digits[i]!=9:
                digits[i]+=1
                return digits
            else:
                digits[i]=0
                i-=1
        if i==-1:
            digits.insert(0,1)
        return digits
