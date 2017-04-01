"""
149. Max Points on a Line Add to List
DescriptionSubmissionsSolutions
Total Accepted: 75450
Total Submissions: 486811
Difficulty: Hard
Contributors: Admin
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

Hide Company Tags LinkedIn Apple Twitter
Hide Tags Hash Table Math
Hide Similar Problems (M) Line Reflection

"""
#[[0,0],[94911151,94911150],[94911152,94911151]]
# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b
import numpy as np


class Solution(object):

    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        l = len(points)
        m = 0
        for i in range(l):
            dic = {'i': 1}
            same = 0
            for j in range(i + 1, l):
                tx, ty = points[j].x, points[j].y
                #consider the same point
                if tx == points[i].x and ty == points[i].y:
                    same += 1
                    continue
                #the slope is infinite
                if points[i].x == tx:
                    slope = 'i'
                else:
                    #consider slope is out of the limit of double data type.
                    slope = np.longdouble(
                        points[i].y - ty) / (points[i].x - tx)

                if slope not in dic:
                    dic[slope] = 1
                dic[slope] += 1
            for i in dic.values():
                # print i
            m = max(m, max(dic.values()) + same)
        return m
