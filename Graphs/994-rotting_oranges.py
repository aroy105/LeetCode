import collections
class Solution:
    """
    You are given an m x n grid where each cell can have one of three values:
        - 0 representing an empty cell,
        - 1 representing a fresh orange, or
        - 2 representing a rotten orange.
    Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
    Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
    """
    # Since the rot radiates outward at an equal pace, BFS is ideal here
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Store rotting oranges in a deque
        q = collections.deque()
        # Store a global variable for # of fresh oranges and time elapsed
        fresh, time = 0, 0
        
        # Go through the graph, find how many fresh oranges, and store location of rotting ones
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        # While there are fresh oranges and rotting oranges that haven't spread their rot...
        while fresh > 0 and q:
            length = len(q)
            # This method lets us go from generation to generation of rotting oranges
            for i in range(length):
                # Pop from and grab the coordinates of the leftmost rotting orange in this generation
                r, c = q.popleft()
                # Go in all four cardinal directions and continue BFS
                for dr, dc in directions:
                    row, col = r+dr, c+dc
                    # If the new space which is about to be rotten is in bounds and actually has an orange to rot...
                    if (
                        row in range(len(grid))
                        and col in range(len(grid[0]))
                        and grid[row][col] == 1
                    ):
                        # Turn the fruit rotten, add it to q, and update # of fresh fruit
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh -= 1
                        
            # At this point, the current generation of rotten orange have spread to the next gen
            time += 1
        
        # If there are no more fresh fruit remaining, return the time it took for all to become rotten.
        return time if fresh == 0 else -1
                        
