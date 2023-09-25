class Solution:
    """
    You are given an array prices where prices[i] is the price of a given stock on the ith day.
    Find the maximum profit you can achieve. 
    You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:
    After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
    Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
    """
    def maxProfit(self, prices: List[int]) -> int:
        # We can essentially make a decision tree, where our decisions are buy/cooldown, sell/cooldown, cooldown, and repeat
        # Our tree will have a depth of n, and whereas the tree soln would be O(2^n) (2 decisions each time) a cache brings it down to O(n)
        
        # Buying jumps i (the day) by 1, since we have freedom to sell the next day
        # Selling jumps i by 2, since we need to cooldown by at least a day, so our next option to buy is the day after tomorrow
        # Our dict will store a tuple as a key (day, whether we buy or not), and the max profit so far
        dp = {} # Key = (i, buying): Value = max_profit
        
        # Create our DFS solution
        def dfs(i, buying):
            # Base case where if the i value exceeds the number of days, just return 0
            if i >= len(prices):
                return 0
            # If we already have the solution for this particular case cached from a prior calculation, return it
            if (i, buying) in dp:
                return dp[(i, buying)]
            # This represents the case where we just wait a day
            cooldown = dfs(i + 1, buying)
            # If we are buying
            if buying:
                # This is the value if we choose to buy, and store this value in the cache (max between buying then or waiting)
                buy = dfs(i + 1, not buying) - prices[i]
                dp[(i, buying)] = max(buy, cooldown)
            # If we are selling
            else:
                # This is the value if we choose to sell, and store this value in the cache (max between selling or waiting)
                sell = dfs(i + 2, not buying) + prices[i]
                dp[(i, buying)] = max(sell, cooldown)
            # Return the value for this day and buy/sell state
            return dp[(i, buying)]

        # We can either buy or wait on the first day, the wait case is handled since we always check the max between buying now and the cooldown option
        return dfs(0, True)
            