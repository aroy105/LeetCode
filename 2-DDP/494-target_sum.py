class Solution:
    """
    You are given an integer array nums and an integer target.
    You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.
    For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
    Return the number of different expressions that you can build, which evaluates to target.
    """
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Brute force is 2^n, since each choice is binary
        # Memoization is able to make it O(n*total)
        # Our cache will store key: val = (index, total so far): # of ways
        dp = {}
        
        # Now we'll build our backtracking algo
        def backtrack(i, total):
            # If the current index is at the end of the list, return 1 if the returned total is == target, otherwise return 0 (this just means there's 1 way or zero ways from that last spot)
            if i == len(nums):
                return 1 if total == target else 0
            # If we already have the result in the cache, just return the result
            if (i, total) in dp:
                return dp[(i, total)]
            # # of ways at current index = # of ways if we add the value to running total + # of ways if we subtract the value from running total
            dp[(i, total)] = backtrack(i + 1, total + nums[i]) + backtrack(i + 1, total - nums[i])
            # Return the # of ways at this current index
            return dp[(i, total)]
        # Start at backtracking at index zero with the running total set to 0
        return backtrack(0, 0)