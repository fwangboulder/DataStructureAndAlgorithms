"""
45. Jump Game II   Add to List QuestionEditorial Solution  My Submissions
Total Accepted: 83307
Total Submissions: 320202
Difficulty: Hard
Contributors: Admin
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)

Note:
You can assume that you can always reach the last index.

Hide Tags Array Greedy
"""
class Solution(object):
    def jump(self, A):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(A) <= 1:
            return 0
        step, max_range, next_range = 1, A[0], A[0]
        for i in xrange(1,len(A)):
            if max_range >= len(A)-1:
                return step
            if i > max_range:
                max_range = next_range
                step += 1
            next_range = max(next_range, i + A[i])
        return step
