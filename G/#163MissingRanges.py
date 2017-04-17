"""
163. Missing Ranges Add to List
DescriptionHintsSubmissionsSolutions
Total Accepted: 26126
Total Submissions: 102255
Difficulty: Medium
Contributor: LeetCode
Given a sorted integer array where the range of elements are in the inclusive range [lower, upper], return its missing ranges.

For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99, return ["2", "4->49", "51->74", "76->99"].

Hide Company Tags Google
Hide Tags Array
Hide Similar Problems (M) Summary Ranges

"""

class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        pre=lower-1
        res=[]
        nums.append(upper+1)
        for i in nums:
            if i==pre+2:
                res.append(str(pre+1))
            elif i>pre+2:
                res.append(str(pre+1)+"->"+str(i-1))
            pre=i
        return res
