class Solution:
    """
    You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. 
    All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. 
    Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.
    Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
    """
    def rob(self, nums: List[int]) -> int:
        # We can basically just run the first house robber problem on subarrays of this problem
        # We can run it on everything from the first house to the penultimate house, skipping the last house, or we can do second to last house, skipping the first house.
        # There is an edge case we need to watch for, since below, the first case explicitly skips the first element, and the second case skips the last
        # Neither of these will return anything if there's only one house lol
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))
    
    def helper(self, nums):
        """This is just house robber problem"""
        rob1, rob2 = 0, 0
        for n in nums:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp 
        return rob2