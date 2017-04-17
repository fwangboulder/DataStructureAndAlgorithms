"""
340. Longest Substring with At Most K Distinct Characters Add to List
DescriptionHintsSubmissionsSolutions
Total Accepted: 19983
Total Submissions: 51998
Difficulty: Hard
Contributor: LeetCode
Given a string, find the length of the longest substring T that contains at most k distinct characters.

For example, Given s = “eceba” and k = 2,

T is "ece" which its length is 3.

Hide Company Tags Google
Hide Tags Hash Table String
Hide Similar Problems (H) Longest Substring with At Most Two Distinct Characters (M) Longest Repeating Character Replacement

"""
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        d={}
        res=0
        start=0
        for i,v in enumerate(s):
            #check len(d)
            d[v]=d.get(v,0)+1
            #>k
            while len(d)>k:
                res=max(i-start,res)
                d[s[start]]-=1
                if d[s[start]]==0:
                    d.pop(s[start])
                start+=1

            #not >k
            res=max(res,i-start+1)
        return res
                
