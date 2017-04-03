"""
150. Evaluate Reverse Polish Notation Add to List
DescriptionSubmissionsSolutions
Total Accepted: 87459
Total Submissions: 331509
Difficulty: Medium
Contributors: Admin
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
Hide Company Tags LinkedIn
Hide Tags Stack
Hide Similar Problems (H) Basic Calculator (H) Expression Add Operators

"""


class Solution(object):

    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for i in tokens:
            if i.lstrip('-').isdigit():
                stack.append(int(i))

            elif stack:
                b = stack.pop()
                a = stack.pop()
                if i == '+':
                    res = a + b
                elif i == '-':
                    res = a - b
                elif i == '*':
                    res = a * b
                else:
                    res = int(float(a) / b)
                stack.append(res)
        return stack[-1]
