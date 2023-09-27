class Solution:
    """
    You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums.
    You are asked to burst all the balloons.
    If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as
    if there is a balloon with a 1 painted on it.
    Return the maximum coins you can collect by bursting the balloons wisely.
    """
    def maxCoins(self, nums: List[int]) -> int:
        # O(n^3) time complexity, O(n^2) memory
        # This is a pretty hard problem
        # We need to thik about an intelligent subproblem
        # In this case, the subproblem can't be the case where one balloon is popped
        # That would mean we have 2^n subproblems, which is huge
        
        # If we assume we pop one, then consider the remaining balloons. It is broken up into two contiguous subarrays
        # For some array of size n, there are then at most n^2 subarrays (1 of size n, 2 of size n/2, etc etc)
        # This is better, but we still can't do this, since technically, the remaining subarrays are next to each other, and need to be considered holistically
        # For instance, if our list is [3, 1, 5, 8], and we pop the 5, we then have [3, 1, 8]. Popping the 1 gives us 24 points, but if we considered [3, 1] and [8] 
        # separately, we'd have max([3, 1]) = 6 and max([8]) = 8
        
        # If we instead consider popping that one last, then the same contiguous subarrays are never next to each other. In the same case, If [3,1] and [8] got popped first,
        # we never need to worry about the whole [3, 1, 8] state. Thus, we can then pop the continguous subarrays independently
        
        # Remember, there are implicit "1" balloons as placeholders, but for our subarrays, the "last-popped" balloon will be one of the implicit edge balloons
        # Our cache will store the L and R pointer of the subarray, since that basically tells us the subarray we're dealing with currently
        cache = {}
        # Modify it so that we have our "1" balloons
        nums = [1] + nums + [1]
        # We use offset to define the size of the subarray. It's we will usually just set left to be some number, and then right will be left+offset
        # This way, we first look at subarrays of size one, then two, and so on
        for offset in range(2, len(nums)):
            # We start left ptr at 0, and then end up at the last possible point, which is right before the last possible number
            for left in range(len(nums) - offset):
                # Create the right pointer
                right = left + offset
                # Pivot will be the number we are basically removing last. Note, we start directly after left, and end just before hitting the right pointer
                for pivot in range(left + 1, right):
                    # Calculate the coins we'd get from removing the pivot last. If it's last, everything between it and the balloons at the left and right ptr are gone
                    # For example, 1, [3, 1, 5, 8], 1 -> if 5 is being popped last, 3, 1, and 8 are gone, so array is 1[5]1 = 1*5*1. Same deal for all subrarrays
                    coins = nums[left] * nums[pivot] * nums[right]
                    # For the entire case, we still need to add coins we got by popping the other balloons. Thus, add up the subarrays from l:pivot and pivot:r
                    coins += cache.get((left, pivot), 0) + cache.get((pivot, right), 0)
                    # coins now holds the value for the case where we popped the pivot balloon last. 
                    # Store the pivot which yielded the highest sum in the cache
                    cache[(left, right)] = max(coins, cache.get((left, right), 0))
        # If we set the subarray to the entire array, we should now get our answer
        return cache.get((0, len(nums) - 1), 0)