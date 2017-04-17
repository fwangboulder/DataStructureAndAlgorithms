"""
394. Decode String Add to List
DescriptionHintsSubmissionsSolutions
Total Accepted: 26130
Total Submissions: 63984
Difficulty: Medium
Contributor: LeetCode
Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
Hide Company Tags Google
Hide Tags Depth-first Search Stack
Hide Similar Problems (H) Encode String with Shortest Length

"""
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        return self.dfs(s)

    def dfs(self,s):
        if s.isalpha():
            return s
        res = ""
        stack = []
        for i in range(len(s)):
            if not stack and s[i].isalpha():
                res += s[i]
            if s[i]=='[':
                stack.append(i)
            if s[i]==']':
                left = stack.pop()
                if not stack:
                    num_start = left-1
                    while s[num_start].isdigit():
                        num_start -= 1
                    repeat = int(s[num_start+1:left])
                    res += repeat*self.dfs(s[left+1:i])
                    print res
        return res        
