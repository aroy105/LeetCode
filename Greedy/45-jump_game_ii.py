class Solution:
    """
    You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
    Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:
        - 0 <= j <= nums[i] and
        - i + j < n
    Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].
    """
    def jump(self, nums: List[int]) -> int:
        # We can use BFS, and create segments of numbers. Each interval can be segmented by the minimum number of jumps it takes to reach that number
        l, r = 0, 0
        res = 0 
        # While our right boundary of the segment has not exceeded the size of nums...
        while r < (len(nums) - 1):
            # Go through every element in the segment, and find the maximum jump you can take. This will be stored relative to the 0th index.
            maxJump = 0
            for i in range(l, r + 1):
                maxJump = max(maxJump, i + nums[i])
            # Create a new segment, and reset l to be right after our old r
            l = r + 1
            # set new r to maxJump, since this is the edge of the new boundary for the next segment
            r = maxJump 
            # Update res to indicate we're in new segment.
            res += 1
        # Return segment
        return res