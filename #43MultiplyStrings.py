"""
43. Multiply Strings   Add to List QuestionEditorial Solution  My Submissions
Total Accepted: 88771
Total Submissions: 341075
Difficulty: Medium
Contributors: Admin
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2.

Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
Hide Company Tags Facebook Twitter
Hide Tags Math String
Hide Similar Problems (M) Add Two Numbers (E) Plus One (E) Add Binary (E) Add Strings

"""
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if not num1 or not num2:
            return ''
        product=[0]*(len(num1)+len(num2))


        pos=len(product)-1
        for n1 in reversed(num1):
            tmppos=pos
            for n2 in reversed(num2):
                product[tmppos]+=int(n1)*int(n2)
                product[tmppos-1]+=product[tmppos]/10
                product[tmppos]=product[tmppos]%10
                tmppos-=1
            pos-=1
        start=0
        while start<len(product)-1 and product[start]==0:
            start+=1
        return ''.join(map(str,product[start:]))

                
