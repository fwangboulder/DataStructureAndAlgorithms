"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
Hide Tags Backtracking
Hide Similar Problems (M) Combination Sum (M) Permutations

"""
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        r = self.myCombine(0, n, 0, k)
        return r

    def myCombine(self, start, n, depth, k):
        if depth == k:
            return [[start]]
        r = []
        for i in range(start + 1, n  + 1 - (k - depth - 1)):
            t = self.myCombine(i, n, depth + 1, k)
            if start == 0:
                r += t
            else:
                for p in t:
                    p = [start] + p
                    r.append(p)
        return r
    
