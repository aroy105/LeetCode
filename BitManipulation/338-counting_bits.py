class Solution:
    """Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i."""
    def countBits(self, n: int) -> List[int]:
        # O(n) time complexity, since we use DP.
        # If we were to count the 1s in each number, it takes log_2(n) steps, as we divide by the largest power of 2 in each step. Across all n numbers, it would be O(nlog(n))
        
        # This is our array that we will use, since we need it to have every number from 0 to n
        dp = [0] * (n + 1)
        
        # If we observe the binary representations of each number, we'll notice there's a lot of repeated work, especially to the right of the MSB
        # Notice if we only consider the 1s place. We have 0 and a 1. We store these as dp[0], and dp[1] = 1 + dp[n - 1] (n = 1 in this case)
        # Next, look at ten's place. We only have 10 and 11. If we wanted to calculate the # of 1s from 10 - 11, we have 1 + dp[n - 2], for n = 2 and 3. 
        # Then, consider the hundred's place. We then have 100, 101, 110, 111. This is just a repeat of everything from 00 to 11, with an extra 1. Each one is then 1 + dp[n - 4], for n = 4 to 7
        # Note the x term in dp[n - x] always changes when i is the next power of two. For instance, from n = 1 to 7, we have x be [1, 2, 2, 4, 4, 4, 4]
        offset = 1
        # Since the result for dp[0] is already initialized, we can just go from 1 to the end of the list
        for i in range(1, n + 1):
            # offset is our accrued power of 2 value i.e. the 'x' term in dp[n - x]. When i is a new power of two (2 * previous power of two), reset our offset to this new power. 
            if offset * 2 == i:
                offset = i
            # Calculate it as 1 + dp[n - x]
            dp[i] = 1 + dp[i - offset]
        # Then, return the list
        return dp