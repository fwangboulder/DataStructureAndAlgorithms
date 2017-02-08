"""
39. Combination Sum   Add to List QuestionEditorial Solution  My Submissions
Total Accepted: 136485
Total Submissions: 378596
Difficulty: Medium
Contributors: Admin
Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [2, 3, 6, 7] and target 7,
A solution set is:
[
  [7],
  [2, 2, 3]
]
Hide Company Tags Snapchat Uber
Hide Tags Array Backtracking
Hide Similar Problems (M) Letter Combinations of a Phone Number (M) Combination Sum II (M) Combinations (M) Combination Sum III (M) Factor Combinations (M) Combination Sum IV
"""
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        if not candidates:
            return []
        candidates.sort()
        res=[]
        path=[]
        self.dfs(candidates,target,res,path,0)
        return res
    def dfs(self,nums,target,res,path,index):

        if target==0:
            res.append(path)
            return

        for i in range(index,len(nums)):
            if target<nums[index]:
                break
            self.dfs(nums,target-nums[i],res,path+[nums[i]],i)
       
