"""
42. Trapping Rain Water   Add to List QuestionEditorial Solution  My Submissions
Total Accepted: 97754
Total Submissions: 275588
Difficulty: Hard
Contributors: Admin
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example,
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Hide Company Tags Google Twitter Zenefits Amazon Apple Bloomberg
Hide Tags Array Stack Two Pointers
Hide Similar Problems (M) Container With Most Water (M) Product of Array Except Self (H) Trapping Rain Water II

"""
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res=0
        l,r=0,len(height)-1
        while l<r:
            i=1
            if height[l]<height[r]:
                while height[l]>height[l+i]:
                    res+=height[l]-height[l+i]
                    i+=1
                l+=i
            else:
                while height[r]>height[r-i]:
                    res+=height[r]-height[r-i]
                    i+=1
                r-=i
        return res
##method 2 use stack
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #use stack
        s=[]
        res=0
        if not height:
            return 0
        for i in range(len(height)):
            #print height[i]
            if not s or height[i]<height[s[-1]]:
                s.append(i)
            else:
                while s and height[i]>height[s[-1]]:
                    index=s.pop()
                    if not s:
                        break
                    else:

                        #print i, index
                        res+= (min(height[s[-1]], height[i])-height[index])*(i-s[-1]-1)
                s.append(i)
            print s,res
        return res
