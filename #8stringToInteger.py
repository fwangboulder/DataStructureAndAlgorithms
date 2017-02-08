"""
8. String to Integer (atoi)   Add to List QuestionEditorial Solution  My Submissions
Total Accepted: 146571
Total Submissions: 1060691
Difficulty: Easy
Contributors: Admin
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.

Update (2015-02-10):
The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button  to reset your code definition.

spoilers alert... click to show requirements for atoi.

Hide Company Tags Amazon Microsoft Bloomberg Uber
Hide Tags Math String
Hide Similar Problems (E) Reverse Integer (H) Valid Number
"""
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        int_max=2**31-1
        int_min=-2**31
        #check none situation

        #check only whitespace situation
        str=str.strip()
        if not str:
            return 0
        #check + - situation
        flag=1
        if str[0] in ["+","-"]:
            if str[0]=='-':
                flag=-1
            str=str[1:]
        #check if the first char is number
        if not str or not str[0].isdigit():
            return 0
        #ignore all chars after the first no-number char
        for i, v in enumerate(str):
            if not v.isdigit():
                str=str[:i]
                break
        result=0
        for v in str[:]:
            result+=ord(v)-ord('0')
            result*=10
        result/=10
        result*=flag
        if result>int_max:
            return int_max
        elif result<int_min:
            return int_min
        return result
