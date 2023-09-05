class Solution:
    """
    Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.
    A region is captured by flipping all 'O's into 'X's in that surrounded region.
    """
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # To tackle this problem, think about reversing the problem
        # Originally, we are told to capture (only) the surrounded region
        # Rephrase it like this:
        # Capture everything except the unsurrounded region
        ROWS, COLS = len(board), len(board[0])
        # BIG OBSERVATION: A "O" region can only NOT be directionally-surrounded by "X" if at least one of it's grid spaces is touching an edge. 
        
        # Create a DFS Algo that gets triggered when we find an "O" edge block (in below for loops)
        def capture(r, c):
            # If out of bounds and if the grid is an "O"
            if r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != "O":
                return
            # Convert it to a temporary value "T" to indicate it is part of region that remains unconquered. 
            board[r][c] = "T"
            # Run DFS
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)
        
        # In our first iteration across all the grids, if a space is an "O" and it is along the edge of the board, run DFS and find all the unconquerable "O"'s
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r in [0, ROWS - 1] or c in [0, COLS - 1]):
                    capture(r, c)
        
        # In our second iteration, convert all the remaining O's to X's, as they've been conquered.
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        # In our third iteration, convert all the unconquerable "O"s, which were temporarily converted to "T"s, back to "O"s
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] == "O"