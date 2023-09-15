class Solution:
    """Given an integer array nums, return the length of the longest strictly increasing subsequence."""
    def lengthOfLIS(self, nums: List[int]) -> int:
        # We'll create a DP cache which stores the longest strictly increasing subsequence from that point
        LIS = [1] * len(nums)
        # Set up bottom up approach
        for i in range(len(nums) - 1, -1, -1):
            # Test from right after the i pointer to the end of the array
            for j in range(i + 1, len(nums)):
                # If the starting point is less than the value at the 
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        # I initially thought that we need to check j against it's j-1 value, so that it is strictly increasing
        # However, I believe this behavior is handled since we start from the end and work backwards, so the nums[i] < nums[j] is preserved as we push i back 
        # Grab the longest increasing subsequence from the list
        return max(LIS)
                