"""
15. 3Sum   Add to List QuestionEditorial Solution  My Submissions
Total Accepted: 177282
Total Submissions: 844847
Difficulty: Medium
Contributors: Admin
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
Hide Company Tags Amazon Microsoft Bloomberg Facebook Adobe Works Applications
Hide Tags Array Two Pointers
Hide Similar Problems (E) Two Sum (M) 3Sum Closest (M) 4Sum (M) 3Sum Smaller
Have
"""


class Solution(object):

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i, v in enumerate(nums):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            tmp = nums[i]

            li = i + 1
            ri = len(nums) - 1
            while li < ri:
                sums = tmp + nums[li] + nums[ri]
                if sums == 0:
                    res.append([tmp, nums[li], nums[ri]])
                    li += 1
                    ri -= 1
                    while li < ri and nums[ri] == nums[ri + 1]:
                        ri -= 1
                    while li < ri and nums[li] == nums[li - 1]:
                        li += 1

                elif sums > 0:
                    ri -= 1
                    while li < ri and nums[ri] == nums[ri + 1]:
                        ri -= 1
                else:
                    li += 1
                    while li < ri and nums[li] == nums[li - 1]:
                        li += 1

        return res
