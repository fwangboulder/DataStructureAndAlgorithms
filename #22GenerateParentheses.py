"""
22. Generate Parentheses   Add to List QuestionEditorial Solution  My Submissions
Total Accepted: 125655
Total Submissions: 299017
Difficulty: Medium
Contributors: Admin
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
Hide Company Tags Google Uber Zenefits
Hide Tags Backtracking String
Hide Similar Problems (M) Letter Combinations of a Phone Number (E) Valid Parentheses
"""

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res=[]
        s=""
        if n:
            self.dfs(res,s,n,n)
        return res
    def dfs(self,res,s,l,r):
        if l==0 and r==0:
            res.append(s)
        if l>r:
            return
        if l>0:
            self.dfs(res,s+'(',l-1,r)
        if r>0:
            self.dfs(res,s+')',l,r-1)
