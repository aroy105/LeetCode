class Solution:
    """Given an m x n matrix, return all elements of the matrix in spiral order."""
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Similar to rotate image, we'll have a decreasing rectangle we examine as we go from outer to inner layer
        # However, we don't have a square i.e. we can't reuse l, r as top, bottom, so we need extra top and bottom pointers
        # Note right and bottom are actually outer boundaries, which helps when we iterate along those boundaries
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        # Values will be spit out here
        res = []
        
        # Our terminating conditions are similar to rotate-image. Once the barrier pointers equal each other, our area we need to traverse has shrunk all the way
        while left < right and top < bottom:
            # Go through the top boundary of our current area, and then move the top pointer down, since we're switching directions
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1
            # Go down right boundary, and then move the right pointer one spot to the left
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1
            # If we cannot go any further in our spiral i.e. left or up because the left/right or top/bottom pointers crossed over, then just break, since we have completed spiral order
            if not (left < right and top < bottom):
                break
            # Go along the bottom boundary, and move the bottom pointer up
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1
            # Go along the left boundary, and move the left pointer one spot to the right
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
        
        # Once we've finished spiral order, return our answer
        return res
            
            