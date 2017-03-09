"""
16. 3Sum Closest   Add to List QuestionEditorial Solution  My Submissions
Total Accepted: 110204
Total Submissions: 360228
Difficulty: Medium
Contributors: Admin
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Hide Company Tags Bloomberg
Hide Tags Array Two Pointers
Hide Similar Problems (M) 3Sum (M) 3Sum Smaller

"""


class Solution(object):

    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = len(nums)
        dif = 2**31 - 1
        nums.sort()
        print nums
        for i in range(l - 2):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            v = nums[i]
            li, ri = i + 1, l - 1
            while li < ri:
                t = v + nums[li] + nums[ri]
                tmp = abs(t - target)
                if tmp < dif:
                    dif = tmp
                    res = t
                if target == t:
                    return t
                elif target > t:
                    li += 1
                    while li < ri and nums[li] == nums[li - 1]:
                        li += 1
                else:
                    ri -= 1
                    while li < ri and nums[ri] == nums[ri + 1]:
                        ri -= 1
        return res
