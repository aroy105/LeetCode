from collections import deque
# Both solutions don't seem to be super efficient compared to others on LeetCode.
class Solution:
    """
    Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
    An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
    You may assume all four edges of the grid are all surrounded by water.
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        # Base cases, if grid or row doesn't exist, return 0
        if not grid or not grid[0]:
            return 0
        
        # We will manually go through rows and columns
        # We will have a counter for islands, and store the nodes we visited as a set
        islands = 0 
        visit = set()
        rows, cols = len(grid), len(grid[0])
        # We create a depth-first search subroutine
        def dfs(r, c):
            # if our r or c is out of bounds, if we hit water, or if we visited the node, exit
            if (
                r not in range(rows)
                or c not in range(cols) 
                or grid[r][c] == "0"
                or (r, c) in visit
            ):
                return
            # Add current node to visit
            visit.add((r,c))
            # Run DFS in all four cardinal directions
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        
        # Iterate through every square in the grid
        for r in range(rows):
            for c in range(cols):
                # If we have a landmass, which is not part of a contiguous landmass yet...
                if grid[r][c] == "1" and (r, c) not in visit:
                    # Indicate we found an island, and discover the rest of its land
                    islands += 1
                    dfs(r, c)
        return islands
    
# BFS Version
class SolutionBFS:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Base Case
        if not grid:
            return 0
        
        # State variables
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0
        # Bredth first search subroutine
        def bfs(r, c):
            # Store neighbors as a 
            q = deque()
            visited.add((r, c))
            q.append((r, c))
            
            while q:
                row, col = q.popleft()
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (
                        (r) in range(rows) 
                        and (c) in range(cols) 
                        and grid[r][c] == "1" 
                        and (r, c) not in visited
                    ):
                        q.append((r, c))
                        visited.add((r, c))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1
        
        return islands