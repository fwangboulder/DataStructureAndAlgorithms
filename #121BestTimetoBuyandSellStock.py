"""
121. Best Time to Buy and Sell Stock Add to List
DescriptionSubmissionsSolutions
Total Accepted: 173882
Total Submissions: 434953
Difficulty: Easy
Contributors: Admin
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.
Hide Company Tags Amazon Microsoft Bloomberg Uber Facebook
Hide Tags Array Dynamic Programming
Hide Similar Problems (E) Maximum Subarray (E) Best Time to Buy and Sell Stock II (H) Best Time to Buy and Sell Stock III (H) Best Time to Buy and Sell Stock IV (M) Best Time to Buy and Sell Stock with Cooldown

"""


class Solution(object):

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        max_p = 0
        min_price = prices[0]
        for i, num in enumerate(prices):
            min_price = min(min_price, num)
            max_p = max(max_p, prices[i] - min_price)
        return max_p
