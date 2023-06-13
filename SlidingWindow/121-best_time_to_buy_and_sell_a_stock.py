class Solution:
    """
    You are given an array prices where prices[i] is the price of a given stock on the ith day.

    You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

    Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
    """
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        # Set the left side of the sliding window to the first element
        # This should be the lowest price we buy stuff at
        lowest = prices[0]
        
        # This will be the right side of our sliding window
        for price in prices:
            # If we find a lower price at which we can buy our stock
            if price < lowest:
                # Set this to the new left side of our sliding window
                lowest = price
            # Each day, check what our max capital appreciation is
            res = max(res, price - lowest)
        
        return res