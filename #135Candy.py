"""
135. Candy Add to List
DescriptionSubmissionsSolutions
Total Accepted: 65521
Total Submissions: 270775
Difficulty: Hard
Contributors: Admin
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?

Hide Tags Greedy
Have you met this question in a real interview? Yes
"""


class Solution(object):

    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """

        candies = [1] * len(ratings)
        for i in xrange(len(ratings) - 1):
            # from left to right
            if ratings[i + 1] > ratings[i]:
                candies[i + 1] = max(candies[i + 1], candies[i] + 1)
            # from right to left
            j = -i - 1
            if ratings[j - 1] > ratings[j]:
                candies[j - 1] = max(candies[j - 1], candies[j] + 1)

        return sum(candies)
