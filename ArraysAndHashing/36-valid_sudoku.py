from collections import defaultdict
class Solution:
    """Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated"""
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set) # Given 9 squares, there are 3 square rows and 3 square columns, so we can pick squares via (r//3, c//3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue # Skips to end of current iteration of loop
                if (
                    board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r//3, c//3)]
                ):
                    return False
                cols[c].add(board[r][c])
                rows[c].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])

        return True
