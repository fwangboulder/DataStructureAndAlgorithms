"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
 LinkedIn Uber Airbnb Facebook Amazon Microsoft Apple Yahoo Dropbox Bloomberg Yelp Adobe
Hide Tags Array Hash Table
Hide Similar Problems (M) 3Sum (M) 4Sum (M) Two Sum II - Input array is sorted (E) Two Sum III - Data structure design

UPDATE (2016/2/13):
The return format had been changed to zero-based indices. Please read the above updated description carefully.
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #step 1 loop over nums
        # step 2 check whether target-cur is in dictionary
                 #if not, store the dif and index as key value pair
                 #if so, return the value for key=diff and index of cur

        d=dict()
        for i,num in enumerate(nums):
            if num not in d:
                d[target-num]=i
            else:
                return [d[num],i]
        return []
