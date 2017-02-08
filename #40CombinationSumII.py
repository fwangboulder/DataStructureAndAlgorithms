"""
40. Combination Sum II   Add to List QuestionEditorial Solution  My Submissions
Total Accepted: 99015
Total Submissions: 313563
Difficulty: Medium
Contributors: Admin
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Hide Company Tags Snapchat
Hide Tags Array Backtracking
Hide Similar Problems (M) Combination Sum

"""

class Solution(object):
    def combinationSum2(self, candidates, target):
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
        index=0
        self.dfs(candidates,target,res,path,index)
        return res
    def dfs(self,nums,target,res,path,index):
        if target==0 and path not in res:
            res.append(path)
            return
        for i in range(index,len(nums)):
            if target<nums[i]:
                break
            self.dfs(nums,target-nums[i],res,path+[nums[i]],i+1)
        
