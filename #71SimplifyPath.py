"""
71. Simplify Path   Add to List QuestionEditorial Solution  My Submissions
Total Accepted: 74518
Total Submissions: 308845
Difficulty: Medium
Contributors: Admin
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
click to show corner cases.

Corner Cases:
Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".
Hide Company Tags Microsoft Facebook
Hide Tags Stack String

"""
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack=[]
        s=[p for p in path.split('/') if p!="." and p!=""]
        for i in s:
            if i=="..":
                if len(stack)>0:
                    stack.pop()
            else:
                stack.append(i)
        return '/'+'/'.join(stack)
