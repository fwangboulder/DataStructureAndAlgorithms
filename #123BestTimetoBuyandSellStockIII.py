"""
123. Best Time to Buy and Sell Stock III Add to List
DescriptionSubmissionsSolutions
Total Accepted: 79978
Total Submissions: 279284
Difficulty: Hard
Contributors: Admin
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Hide Tags Array Dynamic Programming
Hide Similar Problems (E) Best Time to Buy and Sell Stock (E) Best Time to Buy and Sell Stock II (H) Best Time to Buy and Sell Stock IV
Have you met this question in a real interview? Yes
O(n),O(n)
"""


class Solution(object):

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if not prices:
            return 0

        # forward traversal, profits record the max profit
        # by the ith day, this is the first transaction
        profits = []
        max_profit = 0
        current_min = prices[0]
        for price in prices:
            current_min = min(current_min, price)
            max_profit = max(max_profit, price - current_min)
            profits.append(max_profit)

        # backward traversal, max_profit records the max profit
        # after the ith day, this is the second transaction
        total_max = 0
        max_profit = 0
        current_max = prices[-1]
        for i in range(len(prices) - 1, -1, -1):
            current_max = max(current_max, prices[i])
            max_profit = max(max_profit, current_max - prices[i])
            total_max = max(total_max, max_profit + profits[i])

        return total_max
