class Solution:
    """
    Given an m x n integers matrix, return the length of the longest increasing path in matrix.
    From each cell, you can either move in four directions: left, right, up, or down.
    You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).
    """
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # We can basically do this in O(n*m) since we go through every index and only need to run DFS on it once. We store this, and if we've already cached it, skip
        ROWS, COLS = len(matrix), len(matrix[0])
        # Store each Row, Col as the key, and it's value is the longest increasing path from that point
        dp = {} 
        
        # Our DFS algo store coordinates and the value of the previous grid
        def dfs(r, c, prevVal):
            # If out of bounds or if the path we're following is not strictly increasing, return 0 (no valid path)
            if r < 0 or r == ROWS or c < 0 or c == COLS or matrix[r][c] <= prevVal:
                return 0
            # If we've already done the work for this grid, return the result
            if (r, c) in dp:
                return dp[(r, c)]
            # Base Case, every grid is at least a path of length 1
            res = 1
            # Check every cardinal direction for the new max longest path
            res = max(res, 1 + dfs(r + 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c - 1, matrix[r][c]))
            res = max(res, 1 + dfs(r - 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c + 1, matrix[r][c]))
            
            # Cache the result we got. This applies for all intermediary steps in recursive stack, saves a TON of wor
            dp[(r, c)] = res
            return res
        
        # Now, run DFS from every grid point. Note, we use -1, since every element in the grid is at least 0. This guarantees DFS runs at each spot and places a path >= 1
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, -1)
        return max(dp.values())
        