class Solution:
    """
    The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
    Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.
    Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.
    """
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Use a brute force approach here, where row by row we place a queen in an appropriate location 
        # Eensure queens don't land in the same column or diagonal line (rows are already handled by only putting on in each)
        # We can distinguish between diagonals going up and right (positive) and columns going down and right (negative)
        # Notice how the row and column chages with these diagonals
        # Along a negative diagonal, the difference between the row and column will be the same, so track if a queen is on a negative diagonal using this difference. 
        # Along a positive diagonal, the sum between the row and column will be the same, so track using the sum
        
        # Since row is already guaranteed to be unique for each queen, store rest of stuff
        col = set()
        posDiag = set()
        negDiag = set()

        res = []
        board = [["."] * n for i in range(n)]
        
        def backtrack(r):
            # End of rows
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return 
            
            # Go through each column in the current row (i.e. each coordinate). If the coordinate is in a col or diag occupied by another queen, go to the next column
            for c in range(n):
                if c in col or (r+c) in posDiag or (r-c) in negDiag:
                    continue 
                
                # We have found an eligible spot, add a queen here
                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r][c] = "Q"
                # Now that we found an eligible column, go to the next row
                backtrack(r + 1)
                # At this point the recursion needs to be unwound, so remove the added Queen from this spot
                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c] = "."
        
        # Start from row 0 (top row)
        backtrack(0)
        return res