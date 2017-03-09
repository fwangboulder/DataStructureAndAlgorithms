"""
31. Next Permutation   Add to List QuestionEditorial Solution  My Submissions
Total Accepted: 95305
Total Submissions: 338304
Difficulty: Medium
Contributors: Admin
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
Hide Company Tags Google
Hide Tags Array
Hide Similar Problems (M) Permutations (M) Permutations II (M) Permutation Sequence (M) Palindrome Permutation II

"""


class Solution(object):

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        size = len(nums)
        for x in range(size - 1, -1, -1):
            if nums[x - 1] < nums[x]:
                break  # from right to left, find the first descending value as pivot
        if x > 0:
            for y in range(size - 1, -1, -1):
                if nums[y] > nums[x - 1]:
                    nums[x - 1], nums[y] = nums[y], nums[x - 1]
                    break  # from right to left, find the first value larget than pivot
        while x < size - 1:  # reverse the order of nums[x:]
            tmp = nums[x]
            nums[x] = nums[size - 1]
            nums[size - 1] = tmp
            x += 1
            size -= 1
