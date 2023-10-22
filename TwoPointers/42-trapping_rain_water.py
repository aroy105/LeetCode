class Solution:
    """Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining."""
    def trap(self, height: List[int]) -> int:
        # The intuition is that we need to take the minimum of the maximum left and right height at each spot, and subtract the height from each spot. 
        # min(maxL, maxR) - height[i] >= 0
        if not height:
            return 0 # Edge case
        
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        
        # Until our two pointers cross over each other
        while l < r:
            # Take the smaller of the two heights and move it
            if leftMax < rightMax:
                l += 1
                # We only need the value of the leftMax and not the right max, since our logic in the if statement ensures leftMax is the minimum
                # By updating leftMax and taking the larger of the height or previous leftMax, we ensured that leftMax - height[l] >= 0
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                # We only need the value of the rightMax and not the left max, since our logic in the if statement ensures rightMax is the minimum
                # By updating rightMax and taking the larger of the height or previous rightMax, we ensured that rightMax - height[l] >= 0
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        
        return res
                
