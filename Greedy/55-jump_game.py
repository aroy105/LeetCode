class Solution:
    """
    You are given an integer array nums. 
    You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
    Return true if you can reach the last index, or false otherwise.
    """
    # This problem can be done both via DP or Greedy
    # We basically go and push the goal ptr backwards based on whether a previous num can jump to goal.
    # At the end, we see if the goal reached the end. 
    def canJump(self, nums: List[int]) -> bool:
        # This represents the final index, which is our initial goal
        goal = len(nums) - 1
        
        # Start from the penultimate element and go all the way to the end
        for i in range(len(nums) - 2, -1, -1):
            # If the current index + the highest possible jump exceeds or can just reach the goal...
            if i + nums[i] >= goal:
                # bring the goal down to the next checkpoint
                goal = i
        # At this point, we have gone as far back as possible
        # See if a path was created from front to back
        return goal == 0