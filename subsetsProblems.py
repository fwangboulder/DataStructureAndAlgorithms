#! /usr/bin/env python
import unittest
"""
Subsets(#78)
return all possible subsets for your array with no duplicate.
example nums=[1,2,3], return [[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]]


(Unique subsets #90)
return all possible subsets (no duplicate) for your arrary with duplicate.
example nums=[1,2,2], return [[],[1],[2],[1,2],[1,2,2],[2,2]]

"""
class Solution(object):
    def subsets(self, nums):

        """
        :type nums: List[int]
        :rtype: List[List[int]]
        this function returns all possible subsets of the given array.
        Construction: res=[]
        1. Start: []
        2. Put in each elements: [1], [2], [3]
        3. Including the element and get all other possible subsets. This can be achieved using a recursion method.
        """
        nums.sort()
        res=[]
        self.subsetsHelper(nums, 0,[], res)
        return res
    def subsetsHelper(self, nums, index, lst, res):
        res.append(lst)
        for i in xrange(index,len(nums)):
            # including each element and find subsets-recursion, depth first search
            self.subsetsHelper(nums,i+1,lst+[nums[i]],res)

###########################################
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        Construction: a res array as the result.
        Start with [], then add each element (no duplicate)
        Then including each element and find all possible subsets: recursion, depth first search

        """
        res=[]
        self.subsetsWithDupHelper(nums,0,[],res)
        return res
    def subsetsWithDupHelper(self,nums,index,lst,res):
        res.append(lst)
        for i in xrange(index,len(nums)):
            #ignore the duplicate value
            if i!=index and nums[i]==nums[i-1]:
                continue
            #including each element and repeat the looking for all possible subsets step.
            self.subsetsWithDupHelper(nums,i+1, lst+[nums[i]],res)

#test
case=Solution()
print case.subsets([1])
class test(unittest.TestCase):
    def test_subsets(self):
        self.assertEqual(sorted(case.subsets([])), sorted([[]]))
        self.assertEqual(sorted(case.subsets([1,2,3])), sorted([
              [3],
              [1],
              [2],
              [1,2,3],
              [1,3],
              [2,3],
              [1,2],
              []
            ]))
    def test_subsetsWithDup(self):
        self.assertEqual(sorted(case.subsetsWithDup([1,2,2])), sorted([[],[2],[2,2],[1],[1,2],[1,2,2]]))
        self.assertEqual(sorted(case.subsetsWithDup([1,1])), sorted([[],[1],[1,1]]))

if __name__=="__main__":
    unittest.main()
