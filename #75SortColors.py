"""
75. Sort Colors
Description  Submission  Solutions  Add to List
Total Accepted: 140578
Total Submissions: 381658
Difficulty: Medium
Contributors: Admin
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.

click to show follow up.

Follow up:
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.

Could you come up with an one-pass algorithm using only constant space?
Hide Company Tags Pocket Gems Microsoft Facebook
Hide Tags Array Two Pointers Sort
Hide Similar Problems (M) Sort List (M) Wiggle Sort (M) Wiggle Sort II

"""

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count_0=0
        count_1=0
        count_2=0
        for i in nums:
            if i==0:
                count_0+=1
            elif i==1:
                count_1+=1
            else:
                count_2+=1
        print count_0, count_1,count_2
        if count_0:
            for i in range(count_0):
                nums[i]=0
        if count_1:

            for i in range(count_0,count_1+count_0):
                nums[i]=1
        if count_2:
            for i in range(count_0+count_1, count_2+count_1+count_0):
                nums[i]=2
            
