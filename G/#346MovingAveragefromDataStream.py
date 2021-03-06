"""
346. Moving Average from Data Stream Add to List
DescriptionHintsSubmissionsSolutions
Total Accepted: 20970
Total Submissions: 36042
Difficulty: Easy
Contributor: LeetCode
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

For example,
MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
Hide Company Tags Google
Hide Tags Design Queue
"""
from collections import deque
class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.queue=deque(maxlen=size)




    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.queue.append(val)
        return float(sum(self.queue))/len(self.queue)



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
