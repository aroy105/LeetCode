class Solution:
    """Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram."""
    def largestRectangleArea(self, heights: List[int]) -> int:
        # If we think about it incrementally, when we have consecutive rectangles that increase or stay the same in height, we can kinda extend the rectangle 
        # Thus, if we have a larger rectangle and a smaller rectangle, the larger rectangle needs to be popped
        #
        #               X
        #           X   X
        #       X   X   X
        #   X   X   X   X     In this example, all rectangles in spots 1-4 can be extended further. 
        
        #               X
        #           X   X   X
        #       X   X   X   X
        #   X   X   X   X   X     In this case, only rectangles in spots 1-3 can be extended, and the rectangle in 4 must be popped
        
        # When we pop from the stack, we calculate the max height that we could have gotten from the removed rectangle.
        # We can also push the rectangles starting index from the higher popped index
        maxArea = 0
        stack = [] # pair: (starting index, height)
        
        for i, h in enumerate(heights):
            start = i
            # Check if the previous rectangle is taller than the current rectangle. 
            while stack and stack[-1][1] > h:
                # That previous rectangle can't be extended further...
                index, height = stack.pop()
                # ...and check if it ended up being the largest rectangle
                maxArea = max(maxArea, height*(i - index))
                # We can push the start index of the current (smaller) rectangle all the way back to the starting point of the popped (taller) rectangle
                start = index
            # Now that all taller rectangles have been maxxed out, we can update the current smaller rectangle as far back as possible
            stack.append((start, h))
        
        # Now we may still have some remaining rectangles that could have been extended as far as possible, so we need to check if any of these are the max height
        for i, h in stack:
            # Since these surviving rectangles were able to extend all the way, their width terminates at the end. 
            # We can calculate the width as the total length of the heights, minus wherever the rectangle begins
            maxArea = max(maxArea, h * (len(heights) - i))
        
        return maxArea 