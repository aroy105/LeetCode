class Solution:
    """
    You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
    You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
    """
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Essentially, we rotate everything in the outer layer, then the next layer, and so on until we get to the smallest center square
        # Define the left and right rows
        l, r = 0, len(matrix) - 1
        # We need to terminate when we reach the smallest center square. This is when the left and right pointers are right next to/on top of each other
        # Thus, when l crosses over r pointer, we're going to start rotating square pointers that we already rotated. 
        # E.g. with a 5x5 square, l = 0, r = 4. We do the outermost boundary. Then l = 1 and r = 3, so we do that inner 3x3 square boundary. 
        # Then l = r = 2, which is just the center square, which doesn't need rotation. Anything further, where l = 3 and r = 1 would just rotate everything again
        while l < r:
            # Consider top boundary of the current square. We'll start at the left corner, and rotate this corner + the 3 points on the corresponding boundaries as well
            # Then offset by one spot, and continue. We'll do this until we reach the right corner. This is done by the following for loop. 
            for i in range(r - l):
                # save the current left and right pointers to index into the left and right rows
                top, bottom = l, r
                # To modify things in place, we need to save one point, transpose the previous value here, then the prior to prior value into the prior value, etc.
                # Ultimately, place the saved value in the spot 90 degrees away
                topLeft = matrix[top][l + i]
                # bottom left -> top left, bottom right -> bottom left, top right -> bottom right
                matrix[top][l + i] = matrix[bottom - i][l]
                matrix[bottom - i][l] = matrix[bottom][r - i]
                matrix[bottom][r - i] = matrix[top + i][r]
                # Now, place the saved top left value into the top right position
                matrix[top + i][r] = topLeft
            # After we go through every point in the boundary, increment the pointers
            r -= 1
            l += 1