class Solution:
    """
    You are given an m x n integer matrix matrix with the following two properties:
    1) Each row is sorted in non-decreasing order.
    2) The first integer of each row is greater than the last integer of the previous row.
    Given an integer target, return true if target is in matrix or false otherwise.
    You must write a solution in O(log(m * n)) time complexity.
    """
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Basically do Binary Search on columns, then rows
        ROWS, COLS = len(matrix), len(matrix[0])
        
        top, bot = 0, ROWS - 1 # TOP is the lower-valued column pointer, BOT is the higher valued column pointer (name describes position)
        # Iterating via columns
        while top <= bot:
            # first row we will inspect
            row = (top + bot) // 2 
            # If our value is greater than the max value in this row
            if target > matrix[row][-1]:
                top = row + 1
            # If our value is smaller than min value in this row
            elif target < matrix[row][0]:
                bot = row - 1
            else: 
                # If we have a potential row narrowed down for our target value...
                break 
            
            # At this point, we either have a potential row, our or top pointer exceeded the bot pointer
            
            # Our pointers should never cross-over, since that means we were not able to converge upon a solution
            # This particular bit apparenty helps clear cases where there is only one entry in the list, because apparently, top > bot just skips out and doesn't even check that entry?
            if not (top <= bot):
                return False
            
            row = (top + bot) // 2 
            l, r = 0, COLS - 1 
            while l <= r:
                m = (l + r) // 2
                if target > matrix[row][m]:
                    l = m + 1 
                elif target < matrix[row][m]:
                    r = m - 1
                else:
                    return True 
            # L and r crossed over i.e. solution was not found
            return False