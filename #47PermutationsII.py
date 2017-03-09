"""
47. Permutations II   Add to List QuestionEditorial Solution  My Submissions
Total Accepted: 103183
Total Submissions: 331139
Difficulty: Medium
Contributors: Admin
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
Hide Company Tags LinkedIn Microsoft
Hide Tags Backtracking
Hide Similar Problems (M) Next Permutation (M) Permutations (M) Palindrome Permutation II
"""


class Solution(object):

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # DFS

        res, visited = [], [False] * len(nums)
        nums.sort()
        self.dfs(nums, visited, [], res)
        return res

    def dfs(self, nums, visited, path, res):
        if len(nums) == len(path):
            res.append(path)
            return
        for i in xrange(len(nums)):
            if not visited[i]:
                if i > 0 and not visited[
                        i -
                        1] and nums[i] == nums[
                        i -
                        1]:  # here should pay attention
                    continue
                visited[i] = True
                self.dfs(nums, visited, path + [nums[i]], res)
                visited[i] = False
