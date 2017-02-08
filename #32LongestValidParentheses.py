"""
32. Longest Valid Parentheses   Add to List QuestionEditorial Solution  My Submissions
Total Accepted: 84316
Total Submissions: 365154
Difficulty: Hard
Contributors: Admin
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.

Hide Tags Dynamic Programming String
Hide Similar Problems (E) Valid Parentheses
Have you met this question in a real interview? Yes  No
DiscussTop Solutions Pick One

"""
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        #use stack, push the index value and pop out if there is a pair.
        # in the end check len(s)-index number
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        res=0
        stack=[]
        for i, n in enumerate(s):
            if not stack:
                stack.append(i)
            else:
                if n==')' and s[stack[-1]]=='(':
                    stack.pop()
                else:
                    stack.append(i)
        end=len(s)
        if not stack:
            return end
        while stack:
            start=stack.pop()
            res=max(res,end-start-1)
            end=start
        res=max(res,end)
        return res
