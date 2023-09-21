import heapq
class Solution:
    """
    You are given an n x n integer matrix grid where each value grid[i][j] represents the elevation at that point (i, j).
    The rain starts to fall. At time t, the depth of the water everywhere is t. 
    You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t. 
    You can swim infinite distances in zero time. Of course, you must stay within the boundaries of the grid during your swim.
    Return the least time until you can reach the bottom right square (n - 1, n - 1) if you start at the top left square (0, 0).
    """
    def swimInWater(self, grid: List[List[int]]) -> int:
        # If we think it about it we don't need to track t
        # If we find the path from the top left to the bottom right, that takes the least time, we select for the path with the MINIMUM altitude 
        # We can use a modified greedy algo similar to Djikstra's to solve this problem in O((n^2)log(n))
        
        # Create some of the constants and initialize the data structures we need for this modified Djikstra's 
        N  = len(grid)
        visit = set()
        
        directions = [[1, 0], [0, -1], [0, 1], [-1, 0]] # As always, create a direction matrix that we'll use for graph based movements
        # Our MinHeap will be organized as such, where each coordinate will be associated with the minimum time it takes to get there
        # Note that this minimum time is based on the maximum height it will take to reach that point. Thus, each entry will have three data points
        # The first is the minimum time (or the max height) it'll take to get there, and the 2nd and 3rd coordinates will be the row and column values
        minH = [[grid[0][0], 0, 0]] # Initialize the minheap
        visit.add((0, 0)) # Initialize the visited set
        # Run the BFS underlying Djikstra's
        while minH:
            # Pop the minimum value
            t, r, c = heapq.heappop(minH)
            # If the minimum coordinate is at our final location, return the time
            if r == N - 1 and c == N - 1:
                return t
            # Go in all four directions from this point
            for dr, dc in directions:
                # Create the coordinates in each direction
                neighborR, neighborC = r + dr, c + dc
                # If any of these points are already visited or out of bounds, skip this and go to the next generation
                if (neighborR < 0 or neighborC < 0 or neighborR == N or neighborC == N or (neighborR, neighborC) in visit):
                    continue
                # Add this new coordinate to the visited set
                visit.add(neighborR, neighborC)
                # Add the new coordinate to the minHeap. 
                # Note the t value will always be the highest value so far, so compare the t between the previous coordinate and the new one
                heapq.heappush(minH, [max(t, grid[neighborR][neighborC]), neighborR, neighborC])
                