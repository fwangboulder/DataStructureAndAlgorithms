"""
67. Add Binary   Add to List QuestionEditorial Solution  My Submissions
Total Accepted: 123270
Total Submissions: 401754
Difficulty: Easy
Contributors: Admin
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".

Hide Company Tags Facebook
Hide Tags Math String
Hide Similar Problems (M) Add Two Numbers (M) Multiply Strings (E) Plus One

"""


class Solution(object):

    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        carry:
        aa:
        bb:
        """
        la = len(a)
        lb = len(b)
        maxl = max(la, lb)
        res = ''
        carry = False  # check the carry
        for i in range(maxl):
            aa = False  # check whether a is 1
            bb = False  # check whether b is 1
            newcarry = False  # pass the new carry to carry in the end
            if la - 1 - i >= 0 and a[la - 1 - i] == '1':
                aa = True
            if lb - 1 - i >= 0 and b[lb - 1 - i] == '1':
                bb = True
            if aa and bb:  # both 1
                if carry:
                    res = '1' + res
                else:
                    res = '0' + res
                newcarry = True
            elif aa != bb:  # only one equal to 1
                if carry:
                    res = '0' + res
                    newcarry = True
                else:
                    res = '1' + res
            else:  # both 0
                if carry:
                    res = '1' + res
                else:
                    res = '0' + res
            carry = newcarry
        if carry:
            res = '1' + res
        return res
