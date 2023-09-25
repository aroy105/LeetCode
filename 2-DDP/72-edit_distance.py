class Solution:
    """
    Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
    You have the following three operations permitted on a word:
        - Insert a character
        - Delete a character
        - Replace a character
    """
    def minDistance(self, word1: str, word2: str) -> int:
        # It's always possible to transform word1 to word2, even if word2 is "" i.e. remove all characters from word1
        # From a dynamic programming perspective, if w1[i] == w2[j], just reduce the problem to minDistance(w1[i+1:], w2[j+1:])
        # Our decision tree will just be to insert, delete, and replace a character
        # In this case, insert yields (i, j+1), delete is (i+1, j), and replace is (i+1, j+1) (since we force them to be equal)
        # Base Case: If both strings are zero, return 0, since zero operations are needed to make them zero
        # Our grid will be len(w1) + 1 by len(w2) + 1 (extra row/col for base case)
        # The base case, where for instance we have an empty string from w2, but the entire string from word 1, would return the length of word 1 (# of add operations you must do)
        # If we're at the empty string of w1, but the 3rd to last string of w2, we should return 3, since 3 add operations are needed. We fill the last row and col accordingly.
        
        # Create our grid, populate it with infinity
        dp = [[float("inf")] * (len(word2) + 1) for i in range(len(word1) + 1)]
        # First along the bottom row, then along the right most column, fill it up with the surplus of the other word
        for j in range(len(word2) + 1):
            dp[len(word1)][j] = len(word2) - j
        for i in range(len(word1) + 1):
            dp[i][len(word2)] = len(word1) - i
        # Now, only inspect the character pairing where neither is null (null cases handled above)
        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                # If the words are equal, basically progress to minDistance(w1[i+1:], w2[j+1:])
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                # Otherwise, check which action is cheapest (adding, deleting, or replacing a character)
                else:
                    dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j + 1], dp[i + 1][j + 1])
        # Return the propogated value
        return dp[0][0]