"""
56. Merge Intervals   Add to List QuestionEditorial Solution  My Submissions
Total Accepted: 102948
Total Submissions: 359836
Difficulty: Medium
Contributors: Admin
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].

Hide Company Tags LinkedIn Google Facebook Twitter Microsoft Bloomberg Yelp
Hide Tags Array Sort
Hide Similar Problems (H) Insert Interval (E) Meeting Rooms (M) Meeting Rooms II (M) Teemo Attacking

"""

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution(object):

    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """

        if len(intervals) == 0:
            return intervals
        intervals = sorted(intervals, key=lambda x: x.start)
        res = []
        res.append(intervals[0])
        for interval in intervals:
            if interval.start > res[-1].end:
                res.append(interval)
            else:
                res[-1].end = max(res[-1].end, interval.end)
        return res

# check how to do Merge sort without using built in sort function.
