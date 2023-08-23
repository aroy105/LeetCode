class Solution:
    """Given an integer array nums, find the subarray with the largest sum, and return its sum."""
    def maxSubArray(self, nums: List[int]) -> int:
        # Res will store the greatest sum of a subarray
        res = nums[0]
        # Total will be the sum of whatever subarray we are looking at
        total = 0
        # Go through each number in order
        for n in nums:
            # Add the number to the sum for the subarray
            total += n 
            # If this subarray sum is greater than our previous result, update it
            res = max(res, total)
            # If the subarray count zeros out, we will restart our subarray count, since the max subarray from this point could just go to the next value
            # It's not like where n < 0 could stop us from seeing something like ... -1, 100000000, ...
            if total < 0:
                total = 0
        return res