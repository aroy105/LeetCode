class Solution:
    """Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise."""
    def canPartition(self, nums: List[int]) -> bool:
        # If the sum of all the elements is odd, then there are no two groupings that can be made which add up to sum(nums)
        if sum(nums) % 2:
            return False
        # We have a base case of 0, where obviously if we select 0 elements, we have a sum o f0
        dp = set()
        dp.add(0)
        # This is the value we want a grouping to sum up to
        target = sum(nums) // 2
        # Set up bottom up approach
        for i in range(len(nums) - 1, -1, -1):
            # We can't iterate through our cache while we're adding elements to it, so we make a placeholder cache
            nextDP = set()
            # For each summation in dp
            for t in dp:
                # If the addition of the new value plus our previous sub-sums adds up to the target, immediately return true
                if (t + nums[i]) == target:
                    return True 
                # Otherwise, add this subsum to our DP cache, along with the individual element itself (represents just picking the one element)
                # Remember, the new number itself is also added to the cache, since 0 is a subsum, and 0 + number = number
                nextDP.add(t + nums[i])
                nextDP.add(t)
            # replace our old cache with the updated cache including the new sums from this iteration
            dp = nextDP
        return False