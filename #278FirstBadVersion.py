"""
278. First Bad Version   Add to List QuestionEditorial Solution  My Submissions
Total Accepted: 80829
Total Submissions: 331148
Difficulty: Easy
Contributors: Admin
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.

Hide Company Tags Facebook
Hide Tags Binary Search
Hide Similar Problems (M) Search for a Range (M) Search Insert Position (E) Guess Number Higher or Lower

"""# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):

        """
        :type n: int
        :rtype: int
        """
        return self.binarySearch(1, n)

    def binarySearch(self, low, high):
        if low == high:
            return low
        mid = low+(high-low)/2
        if isBadVersion(mid) == True:
            return self.binarySearch(low, mid)
        else:
            return self.binarySearch(mid , high)
