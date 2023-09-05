from collections import deque
class Solution:
    """
    You are given an m x n grid rooms initialized with these three possible values.
    -1 : A wall or an obstacle 
    0: A Gate 
    INF: Infinity means an empty room. We use the value 2^31 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647
    Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF. 
    """
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # We can use BFS to avoid repeated work
        ROWS, COLS = len(rooms), len(rooms[0])
        visit = set()
        q = deque()
        
        # If we are given a location that is out of bounds, already visited, or a wall, just return
        def addRooms(r, c):
            if (
                min(r, c) < 0
                or r == ROWS
                or c == COLS 
                or (r, c) in visit
                or rooms[r][c] == -1
            ):
                return
            # Now, add this room to both visit and the queue
            visit.add((r, c))
            q.append([r, c])
        
        # Go through every element in the grid, and if it's a gate, include it in the starting queue
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))
        # Initialize the distance from gate variable
        dist = 0
        # Run BFS. While there are rooms we are analyzing...
        while q:
            # Go through all the rooms a distance dist from the nearest gate, and then do neighbors dist + 1
            for i in range(len(q)):
                r, c = q.popleft()
                rooms[r][c] = dist
                addRooms(r + 1, c)
                addRooms(r, c + 1)
                addRooms(r - 1, c)
                addRooms(r, c - 1)
            # Increment distance counter for next "level" of rooms
            dist += 1