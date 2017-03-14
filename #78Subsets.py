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

    def subsets1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        This function produces all possible subsets of nums. Use the iterative method.
        First, store the index and value in a stack one by one and append it to res array.
        Example: nums=[1,2,3]
        First start from 0,
        stack=[(0,1),(1,2),(2,3)]
        res=[[1],[1,2],[1,2,3]]
        Second start from 3: stack=[(0,1),(1,2)]
        Third start from 2:stack=[(0,1),(2,3)] res+[[1,3]]
        Fourth start from 1:stack=[(1,2)] res+[[2]]+[[2,3]] +[[3]]+[[]]
        """

        nums.sort()
        res, stack, x, n = [[]], [], 0, len(nums)
        while True:
            if x < n:
                stack += [(x, nums[x])]
                res += [list(zip(*stack)[1])]
                x += 1
            elif stack:
                x = stack.pop()[0] + 1
            else:
                return ans


    def subsets2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        this function produces all possible subsets of nums. Use depth first search
        method. Assume nums=[1,2,3] In depth 0, result array append [], which makes [[]]; In depth 1,
        res=[[],[1],[2],[3]]; In depth 2, res=[[],[1],[2],[3],[1,2],[1,3],[2,3]];
        In depth 3, res=[[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]]
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

    def test_subsets1(self):
        self.assertEqual(sorted(test.subsets1([1,2,3])), sorted([
              [3],
              [1],
              [2],
              [1,2,3],
              [1,3],
              [2,3],
              [1,2],
              []
            ]))
        self.assertEqual(sorted(test.subsets1([])), sorted([[]]))
        self.assertEqual(sorted(test.subsets1([1])), sorted([[1],[]]))

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
