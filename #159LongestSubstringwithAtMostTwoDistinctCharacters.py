"""
159. Longest Substring with At Most Two Distinct Characters Add to List
DescriptionSubmissionsSolutions
Total Accepted: 24186
Total Submissions: 60181
Difficulty: Hard
Contributors: Admin
Given a string, find the length of the longest substring T that contains at most 2 distinct characters.

For example, Given s = “eceba”,

T is "ece" which its length is 3.

Hide Company Tags Google
Hide Tags Hash Table Two Pointers String
Hide Similar Problems (M) Longest Substring Without Repeating Characters (H) Sliding Window Maximum (H) Longest Substring with At Most K Distinct Characters

"""
class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        d={}
        start=0
        max_l=0
        for index,i in enumerate(s):
            d[i]=d.get(i,0)+1
            while len(d)>2:
                max_l=max(max_l,index-start)
                d[s[start]]-=1
                if d[s[start]]==0:
                    d.pop(s[start])
                start+=1
            max_l=max(max_l,index-start+1)
        return max_l
                
