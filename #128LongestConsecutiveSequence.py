"""
128. Longest Consecutive Sequence Add to List
DescriptionSubmissionsSolutions
Total Accepted: 96399
Total Submissions: 268827
Difficulty: Hard
Contributors: Admin
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.

Hide Company Tags Google Facebook
Hide Tags Array Union Find
Hide Similar Problems (M) Binary Tree Longest Consecutive Sequence

"""


class Solution(object):

    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums = set(nums)
        maxLen = 0
        while nums:
            n = nums.pop()
            # go up
            i = n + 1
            l1 = 0
            l2 = 0
            while i in nums:
                nums.remove(i)
                i += 1
                l1 += 1
            # go down
            i = n - 1
            while i in nums:
                nums.remove(i)
                i -= 1
                l2 += 1
            maxLen = max(maxLen, l1 + l2 + 1)
        return maxLen
