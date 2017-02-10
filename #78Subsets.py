"""
78. Subsets
Description  Submission  Solutions  Add to List
Total Accepted: 140775
Total Submissions: 377906
Difficulty: Medium
Contributors: Admin
Given a set of distinct integers, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
Hide Company Tags Amazon Uber Facebook
Hide Tags Array Backtracking Bit Manipulation
Hide Similar Problems (M) Generalized Abbreviation
backpacking
"""
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()
        ans,stack,x,n=[[]],[],0,len(nums)
        while True:
            if x<n:
                stack+=[(x,nums[x])]
                ans+=[zip(*stack)[1]]
                x+=1
            elif stack:
                x=stack.pop()[0]+1
            else:
                return ans
