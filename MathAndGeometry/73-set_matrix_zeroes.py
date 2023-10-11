class Solution:
    """Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's. You must do it in place"""
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Our most inefficient solution would using copy array, which we change based on where 0s are. 
        # We use copy, since changing matrix in place might cause new zeros to propogate and falsely flip other squares. Note, there's a ton of repeated work
        # Our next best solution is to instead make 2 arrays, representing row & column. We go through the matrix, and mark which rows and columns will need to be flipped. Then, we zero at end
        # Our best solution is to just directly put these two arrays over the top row and left column. Thus, we convert our top row and left column to be our reference for what to zero
        # There are slight issues we need to do. Since the square in the top left corner represents both the top row and the left column, we just use a little extra space
        # What we do is keep the top row intacts. Each value corresponds to the column it'll zero out. Then, we'll have the left column all the way up to but not including the top value
        # Each value in the left column represents the row it'll zero out. Then, we keep a litte memory to represent whether we flip the top row. 
        # Note, we can do this, because we never overwrite squares as zeros that should be 1, since we always move down and right
        
        # This solution is O(1) memory. Now, set the bounds for our matrix, and set our boolean for whether we zero out the top row to False
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False
        
        # Go through every element in the matrix
        for r in range(ROWS):
            for c in range(COLS):
                # If the value is zero, set the corresponding value in the left column to zero i.e. zero out the cth row. If r != 0, set rth value in top row to zero i.e. zero out rth column
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True
        
        # Based on stored values in the top row and left column, zero out the smaller (r-1)x(c-1) matrix
        for r in range(1, ROWS):
            for c in range(1, COLS):
                # If either the row or column the square belongs to must be zeroed out, zero it out
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        # If our left column needs to be zeroed out, then zero it out. At this point, it's safe to clobber the left column
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0
        
        # if our top row needs to be zeroed out, then zero it out
        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0