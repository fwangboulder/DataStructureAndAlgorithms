"""
20. Valid Parentheses   Add to List QuestionEditorial Solution  My Submissions
Total Accepted: 164451
Total Submissions: 510034
Difficulty: Easy
Contributors: Admin
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

Hide Company Tags Google Airbnb Facebook Twitter Zenefits Amazon Microsoft Bloomberg
Hide Tags Stack String
Hide Similar Problems (M) Generate Parentheses (H) Longest Valid Parentheses (H) Remove Invalid Parentheses

"""
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        for i in s:
            #print i
            if i in '({[':
                stack.append(i)
                #print stack
            elif i==')' and stack and stack.pop()=="(":
                continue
            elif i==']' and stack and stack.pop()=="[":
                continue
            elif i=='}' and stack and stack.pop()=="{":
                continue
            else:
                return False
        return len(stack)==0
