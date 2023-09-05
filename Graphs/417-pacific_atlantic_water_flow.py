class Solution:
    """
    There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. 
    The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges. 
    The island is partitioned into a grid of square cells. 
    You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).
    The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height
    is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.
    Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.
    """
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # While the intuition may be to visit each node and run dfs on it, there will be a lot of overlap, yielding a O((m*n)^2) complexity. 
        # We can reduce this to O(m*n) by going from the Pacific ocean border, and seeing all the squares it can reach
        # Do the same for the Atlantic Ocean, then find the overlap
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set() # Where we store squares the pacific and atlantic ocean can reach
        
        def dfs(r, c, visit, prevHeight):
            if (
                (r, c) in visit
                or r < 0
                or c < 0
                or r == ROWS
                or c == COLS
                or heights[r][c] < prevHeight # If we can't go from the tile to the ocean, this is the base case
            ):
                return
            visit.add((r, c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])
        
        # Go along the columns
        for c in range(COLS):
            # Run DFS from the top left corner, along the top edge (Pacific Ocean)
            dfs(0, c, pac, heights[0][c])
            # Run DFS from the bottom left corner, along the bottom edge (Atlantic Ocean)
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])
        
        for r in range(ROWS):
            # Run DFS from the top left corner, down the left edge (Pacific Ocean)
            dfs(r, 0, pac, heights[r][0])
            # Run DFS from the top right corner, down the right edge (Atlantic Ocean) 
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])
        
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res