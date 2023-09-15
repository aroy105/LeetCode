class Solution:
    """
    You are a professional robber planning to rob houses along a street. 
    Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems
    connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
    Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
    """
    def rob(self, nums: List[int]) -> int:
        # The recurrence relationship we want to think about to maximize rob is as follows...
        # rob =  max(nums[0] + rob[2:n], rob[1:n])
        # The first part represents us robbing the first house + the value of the max rob sum from all the other houses after we skip the non-adjacent house
        # The second part represents us getting the max rob sum from the second house til the end, skipping the first house
        
        # We will create two running variables store the the max you can rob from 1:x and 1:x+1, representing the two houses
        # rob2 is basically the last house we robbed, and rob1 is the one before that
        # [rob1, rob2, n, n+1]
        rob1, rob2 = 0, 0
        
        # Go through each house
        for n in nums:
            # Compute the maximum we can rob up until n 
            # i.e. current house + all other prior non-adjacent houses (n+rob1) or the previous house + all other prior non-adjacent houses (rob2)
            temp = max(n + rob1, rob2)
            # Now that nth house was robbed, update rob1 and rob2 to be the previous and current house
            rob1 = rob2
            rob2 = temp
            
        # Return the value stored at the last house
        return rob2
            