class Solution:
    """
    You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
    Find two lines that together with the x-axis form a container, such that the container contains the most water.
    Return the maximum amount of water a container can store.
    Notice that you may not slant the container.
    """
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0
        h = max(height)

        while l < r:
            # The bucket will only fill up to the smaller of the left and right end, so the container area will be min(height[l], height[r]) * (r - l)
            res = max(res, min(height[l], height[r]) * (r - l))
            # update the pointer at the lower of the heights
            if height[l] < height[r]:
                l += 1
            elif height[r] <= height[l]:
                r -= 1
            # Neat little optimization, basically if the rectangle formed by the tallest height in the entire heights array and the distance between l and r is smaller than our result, it is impossible for any further buckets to exceed the answer we have already found
            if (r-l) * h <= res:
                break 
        return res