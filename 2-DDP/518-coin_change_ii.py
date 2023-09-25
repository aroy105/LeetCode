class Solution:
    """
    You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
    Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.
    You may assume that you have an infinite number of each kind of coin.
    The answer is guaranteed to fit into a signed 32-bit integer.
    """
    def change(self, amount: int, coins: List[int]) -> int:
        # Brute force is O(c^n) (c is number of coins, n is amount)
        # Memoization gives us O(cn)
        # To not get duplicate combos, we can have higher demomination coin paths never use lower denomination paths
        # Thus, the lowest denomination coin path can use all coins, whereas highest denomination path can't do it
        # There is another solution that is only O(n) for memory though, which basically only maintains two rows. We repeatedly clobber the lower row, and keep the current row we're checking in the top row
        
        # This is the DP solution which is Time: O(n*c), Memory = O(n)
        # We create this bottom row, and set the 0th element to 1. This is because there's 1 way to get 0 coins i.e. choose no coins
        dp = [0]*(amount+1)
        dp[0] = 1
        # Starting from the highest denomination coin to the lowest (remember, combos propogate upwards, so answers will be in the a'th column of the lowest denomination coin)
        for i in range(len(coins)-1, -1, -1):
            # This will be the second column, that will eventually replace the bottom column.
            nextDP = [0]*(amount+1)
            nextDP[0] = 1
            # For amount from 1 cent to amount cents
            for a in range(1, amount+1):
                # Set the ath amount to whatever the total combinations for the amount are so far. 
                nextDP[a] = dp[a]
                # If another combo can be made using the current coin denomination, we can add on the # of combinations from (a - coin) to the current count for this value
                if a - coins[i] >= 0:
                    nextDP[a] += nextDP[a - coins[i]]
            # Clobber and replace our bottom row with the row above.
            dp = nextDP
        # Finally, we have one row, which is the lowest denomination at the amount number
        return dp[amount]