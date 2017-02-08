"""
53. Maximum Subarray   Add to List QuestionEditorial Solution  My Submissions
Total Accepted: 163588
Total Submissions: 420772
Difficulty: Easy
Contributors: Admin
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.

click to show more practice.

Hide Company Tags LinkedIn Bloomberg Microsoft
Hide Tags Array Dynamic Programming Divide and Conquer
Hide Similar Problems (E) Best Time to Buy and Sell Stock (M) Maximum Product Subarray
"""
##The idea is to find the largest difference between the sums when you summing
#up the array from left to right. The largest difference corresponds to the
#sub-array with largest sum. I worked it out independently although It is very
#close to lucastan's solution
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return nums[0]
        res=nums[0]
        Sum=0
        Min=0

        for i in range(0,len(nums)):
            Sum+=nums[i]
            if Sum-Min>res:
                res=Sum-Min
            if Sum<Min:
                Min=Sum
        return res


# o(nlogn) divide and conquer method
"""
Step1. Select the middle element of the array.
So the maximum subarray may contain that middle element or not.

Step 2.1 If the maximum subarray does not contain the middle element, then we can apply the same algorithm to the the subarray to the left of the middle element and the subarray to the right of the middle element.

Step 2.2 If the maximum subarray does contain the middle element, then the result will be simply the maximum suffix subarray of the left subarray plus the maximum prefix subarray of the right subarray

Step 3 return the maximum of those three answer.

Here is a sample code for divide and conquer solution. Please try to understand the algorithm before look at the code


"""
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.maxSubArrayHelper(nums, 0, len(nums) - 1)

    def maxSubArrayHelper(self,nums, l, r):
        if l > r:
            return -2147483647
        m = (l+r) / 2

        leftMax = sumNum = 0
        for i in range(m - 1, l - 1, -1):
            sumNum += nums[i]
            leftMax = max(leftMax, sumNum)

        rightMax = sumNum = 0
        for i in range(m + 1, r + 1):
            sumNum += nums[i]
            rightMax = max(rightMax, sumNum)

        leftAns = self.maxSubArrayHelper(nums, l, m - 1)
        rightAns = self.maxSubArrayHelper(nums, m + 1, r)

        return max(leftMax + nums[m] + rightMax, max(leftAns, rightAns))
