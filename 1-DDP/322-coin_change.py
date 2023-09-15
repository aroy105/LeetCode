class Solution:
    """
    You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
    Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
    You may assume that you have an infinite number of each kind of coin.
    """
    def coinChange(self, coins: List[int], amount: int) -> int:
        # We use dynamic programming, to figure out how many coins it takes to reach each coin denomination
        # Since we start with 0, we need to list the coins it'll take to reach each number from 0 to the amount
        # Amount + 1 will be the basic value, since this is basically Infinity for the purpose of this problem. 
        # Any solution would have to be at least equal to amount i.e. given a 1 cent coin, amount # of coins = amount cents. 
        dp = [amount + 1] * (amount + 1)
        # Naturally it takes zero coins to get to $0
        dp[0] = 0
        # Go through every element in the array
        for a in range(1, amount + 1):
            # Go through each denomination
            for c in coins:
                # If the coin value doesn't exceed the amount...
                # For the longest time, I was stupid and was confused why we don't have a-c == 0. 
                # I thought there were edge case that sounds stupid now, but I thought false positives might come up because I didn't understand the code
                # I thought a false positive would generate where an impossible solutions would just be dp[a-c] incremented by 1, 
                # but the coinage plus a-c might not fully reach a. Obviously that's stupid, since a - c + c = a, I don't know what I was thinking
                # I literally just reviewed the code dumbfounded for half an hour, I am literally an idiot lmao.
                # in case I read this in the future and am confused, 
                # we guarantee this configuration works as long as a - c >= 0 since the coinage to a - c is stored in DP, and then the c coin goes the rest of the way
                if a - c >= 0:
                    # dp[a-c] contains the fewest coins required to reach a-c. 1 + dp[a-c] represents adding the coin to this minimum configuration.
                    # Thus, we update the result if this new configuration is better than the previous or default configuration
                    dp[a] = min(dp[a], 1 + dp[a - c])
        return dp[amount] if dp[amount] != (amount+1) else -1