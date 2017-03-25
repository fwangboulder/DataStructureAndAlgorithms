"""
134. Gas Station Add to List
DescriptionSubmissionsSolutions
Total Accepted: 80188
Total Submissions: 278180
Difficulty: Medium
Contributors: Admin
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

Note:
The solution is guaranteed to be unique.

Hide Tags Greedy

"""


class Solution(object):

    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        pos = -1
        cur = 0
        total = 0
        # loop gas station
        for i in xrange(len(gas)):
            # each step accumulate the diff
            diff = gas[i] - cost[i]
            cur += diff
            total += diff
            # reset the pos if the car cannot move
            if cur < 0:
                cur = 0
                pos = i
        # check if total is enough.
        if total >= 0:
            return pos + 1
        return -1
