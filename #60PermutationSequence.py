"""
60. Permutation Sequence   Add to List QuestionEditorial Solution  My Submissions
Total Accepted: 73905
Total Submissions: 271028
Difficulty: Medium
Contributors: Admin
The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.

Hide Company Tags Twitter
Hide Tags Backtracking Math
Hide Similar Problems (M) Next Permutation (M) Permutations

Recursive Solution

Imagine N = 4 and K = 14
Permutations starting with 1: (2,3,4)! = 6. Total Perms ending with 1 as first element = 6.
Permutations starting with 2: (1,3,4)! = 6. Total Perms ending with 2 as first element = 12.
Permutations starting with 3: (2,1,4)! = 6. Total Perms ending with 3 as first element = 18.
So the 14th permutation should start with 3. The problem reduces to finding the second permutation with input as [1,2 4]. nums = [1,2,4] and K=2.
Permutations starting with 1: (2,4)! = 2. Total Perms ending with 1 as first element = 2.
Permutations starting with 2: (1,4)! = 2. Total Perms ending with 2 as first element = 4.
So the 2nd permutation should start with 1. The problem reduced to finding the second permutation with input as [2,4]. nums = [2,4] and K = 2.
Permutations starting with 2: (4)! = 1. Total Perms ending with 2 as first element = 1
Permutations starting with 4: (2)! = 1. Total Perms ending with 4 as first element = 2
So the 2nd permutation should start with 4. The problem reduces to finding the first permutation with input as [2]. nums = [2] and K = 1. This is the base condition: K=1 just return since nums has the right permutation


"""

class Solution(object):

    def factorial(self, n):
        fact, cache = 1, {0:1}
        for i in range(1, n+1):
            fact *= i
            cache[i] = fact
        return cache

    def helper(self, nums, i, k, cache):
        if k == 1:
            return
        count = 0
        for j in range(i, len(nums)):
            if count + cache[len(nums)-i-1] < k:
                count += cache[len(nums)-i-1]
            else:
                nums[i], nums[j] = nums[j], nums[i]
                nums[i+1:] = sorted(nums[i+1:])
                break
        self.helper(nums, i+1, k-count, cache)
        return

    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        cache, nums = self.factorial(n), [x for x in range(1,n+1)]
        self.helper(nums, 0, k, cache)
        return "".join([str(x) for x in nums])        
