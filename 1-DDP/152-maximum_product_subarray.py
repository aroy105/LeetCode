class Solution:
    """
    Given an integer array nums, find a subarray that has the largest product, and return the product.
    The test cases are generated so that the answer will fit in a 32-bit integer.
    """
    def maxProduct(self, nums: List[int]) -> int:
        # Create a pointer for the result, the current Minimum, and the current maximum
        res = nums[0]
        curMin, curMax = 1, 1
        # Go through every element in nums
        for n in nums:
            # Create a temporary variable, to represent the largest cumulative value * our current element
            tmp = curMax * n 
            # Our current max will be the largest between curMax * n, curMin * n (if n is negative), or n itself for edge cases like [-1, 8]
            # Note for the edge case, it would be best to only have 8, and not any of the other elements
            curMax = max(n * curMax, n * curMin, n)
            # Similarly, we set curMin
            curMin = min(tmp, n * curMin, n)
            # Update res if needed
            res = max(res, curMax)
        return res