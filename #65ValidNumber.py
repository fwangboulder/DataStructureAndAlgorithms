"""
65. Valid Number   Add to List QuestionEditorial Solution  My Submissions
Total Accepted: 61118
Total Submissions: 483435
Difficulty: Hard
Contributors: Admin
Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one.

Update (2015-02-10):
The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button  to reset your code definition.

Hide Company Tags LinkedIn
Hide Tags Math String
Hide Similar Problems (M) String to Integer (atoi)

"""


class Solution(object):

    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()  # remove start and end space
        if not s:
            return False
        n = len(s)
        i = 0
        dotFlag = False
        eFlag = False
        hasDigit = False
        hasSign = False
        while i < n:
            # is digit, means pass the sign location
            if s[i].isdigit():
                i += 1
                hasDigit = True
                hasSign = True
            # is dot, means pass the sign location
            elif not dotFlag and s[i] == '.':
                i += 1
                dotFlag = True
                hasSign = True
            # only when pass first digit, e can start, after e start, can has
            # new sign and new digit, but has no dot
            elif hasDigit and not eFlag and (s[i] == 'e' or s[i] == 'E'):
                i += 1
                dotFlag = True
                eFlag = True
                hasDigit = False
                hasSign = False
            # no digit and no sign, sign flag can start
            elif not hasDigit and not hasSign and (s[i] == '+' or s[i] == '-'):
                i += 1
                hasSign = True
            else:
                return False
        if hasDigit:
            return True
        else:
            return False
