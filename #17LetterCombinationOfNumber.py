"""
17. Letter Combinations of a Phone Number   Add to List QuestionEditorial Solution  My Submissions
Total Accepted: 122900
Total Submissions: 377717
Difficulty: Medium
Contributors: Admin
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.



Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.

Hide Company Tags Amazon Dropbox Google Uber Facebook
Hide Tags Backtracking String
Hide Similar Problems (M) Generate Parentheses (M) Combination Sum (E) Binary Watch
"""
# method 1


class Solution(object):

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        d = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"}

        if not digits:
            return []
        res = ['']
        l = len(digits)
        for i in range(l):
            new_res = []
            for j in res:
                for k in d[digits[i]]:
                    new_res.append(j + k)
            res = new_res
        return res


# Method 2:DFS
class Solution(object):

    def __init__(self):
        self.memo = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"}

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        res = []
        path = ""
        index = 0
        if not digits:
            return res
        self.dfs(digits, res, path, index)
        return res

    def dfs(self, digits, res, path, index):
        if index == len(digits):
            res.append(path)
            return
        for i in self.memo[digits[index]]:
            self.dfs(digits, res, path + i, index + 1)
