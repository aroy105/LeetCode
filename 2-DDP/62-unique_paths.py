from math import factorial
class Solution:
    """
    There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). 
    The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
    Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.
    The test cases are generated so that the answer will be less than or equal to 2 * 10^9.
    """
    def uniquePaths(self, m: int, n: int) -> int:
        # Initially this will be the bottom row
        # Remember, from every square from the bottom row, it can only take one path to the end, so solution from there is obviously 1
        row = [1]*n
        # Now go through the other row
        for i in range(m - 1):
            # Create a row for this column
            newRow = [1]*n
            # To avoid edge cases, we just ignore the right most column, and iterate backwards from penultimate column
            # Similar to the bottom row case, we know values there are always one, since only one path down
            for j in range(n - 2, -1, -1):
                # Each new entry is just the number of combos in the space to the right of it + the space directly below
                newRow[j] = newRow[j + 1] + row[j]
            # Set the new "directly under" row to be our current row, and repeat
            row = newRow
        # Now, we're at the top row, and since we propogated backward, return the value at our origin
        return row[0]
    

# Explicit Solution
# In my combinatorics class, we learned how to solve a similar problem, called lattice path
# We basically have m - 1 right moves, and n - 1 down moves. The answer is just (U + R)!/(U!R!)
    def explicitSoln(self, m, n):
        return factorial(m + n - 2)/(factorial(m - 1)*factorial(n - 1))