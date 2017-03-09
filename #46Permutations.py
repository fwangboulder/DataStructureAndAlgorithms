"""
46. Permutations   Add to List QuestionEditorial Solution  My Submissions
Total Accepted: 143319
Total Submissions: 351659
Difficulty: Medium
Contributors: Admin
Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
Hide Company Tags LinkedIn Microsoft
Hide Tags Backtracking
Hide Similar Problems (M) Next Permutation (M) Permutations II (M) Permutation Sequence (M) Combinations
"""
# dfs


class Solution(object):

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
            return  # backtracking
        for i in xrange(len(nums)):
            self.dfs(nums[:i] + nums[i + 1:], path + [nums[i]], res)
