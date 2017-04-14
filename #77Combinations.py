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
        for i in range(start + 1, n + 1 - (k - depth - 1)):
            t = self.myCombine(i, n, depth + 1, k)
            if start == 0:
                r += t
            else:
                for p in t:
                    p = [start] + p
                    r.append(p)
        return r
#889ms
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        path=[]
        res=[]
        self.dfs(n,k,res,path,1)
        return res
    def dfs(self,n,k,res,path, depth):
        if k==0:
            res.append(path)
            return
        for i in xrange(depth,n+1):
            self.dfs(n,k-1,res,path+[i],i+1)
#255ms
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        I think n-x+1 < k-l is easier to understand.

        One combination has k numbers, and currently we already have l numbers,
        so we need to find another k-l numbers. Since we insert the numbers into
         stack in the ascending order, we want to make sure that there are enough
         larger numbers to be inserted. From x to n, there are n-x+1 numbers
         that are larger than the numbers in the current stack. So if n-x+1 < k-l,
          it means that not enough larger numbers to be inserted, so we track back.
        """

        ans = []
        stack = []
        x = 1
        while True:

            l = len(stack)
            if l == k:
                ans.append(stack[:])
            if l == k or x > n - k + l + 1:
                if not stack:
                    return ans
                x = stack.pop() + 1
            else:
                stack.append(x)
                x += 1
