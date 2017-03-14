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
import unittest


class Solution(object):

    def subsets2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        this function produces all possible subsets of nums.
        """
        res = []
        nums.sort()
        self.dfs(nums, 0, [], res)
        return res

    def dfs(self, nums, index, path, res):
        res.append(path)
        for i in xrange(index, len(nums)):
            if i != index and nums[i] == nums[i - 1]:
                continue
            self.dfs(nums, i + 1, path + [nums[i]], res)


test = Solution()


class Testsubsets(unittest.TestCase):

    def test_subsets2(self):
        self.assertEqual(sorted(test.subsets2([1, 2, 3])), sorted([
            [3],
            [1],
            [2],
            [1, 2, 3],
            [1, 3],
            [2, 3],
            [1, 2],
            []
        ]))
        self.assertEqual(sorted(test.subsets2([])), sorted([[]]))
        self.assertEqual(sorted(test.subsets2([1])), sorted([[1], []]))

if __name__ == "__main__":
    unittest.main()
