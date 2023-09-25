class Solution:
    """
    Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.
    A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without
    changing the relative order of the remaining characters.
    For example, "ace" is a subsequence of "abcde".
    A common subsequence of two strings is a subsequence that is common to both strings.
    """
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Note that with each common character found, we have a new subproblem by just looking at the rest of the substring
        # For example, once a common letter is found, lcs("apple", "ale") = 1 + lcs("pple", "le")
        # Essentially, this algo will mark each matching pair of letters as +1 whatever the max has been so far
        # To do this, we grab the value diagonally to the bottom right of the grid,
        # This represents the pair which is i+1, j+1. There may be an offset where we are checking i = 2 and j = 5, but we're only concerned with the chain from the point 
        # i=3 and j=6 onwards. This grid represents the maximum from all future combinations of incrementing i and j. However, (i=2,j=6) and (i=3,j=5) are invalid points to
        # jump off from since these basically represent removing the common letter from one but not both of the substrings. 
        # If there isn't a matching letter for some indices i and j, then we can just pull the maximum from all the combos originating at (i+1,j) or (i,j+1)
        # This represents jumping over characters that don't match from text1 and text2 respectively.
        
        # First, create the Dynamic Programming Graph, with default values of zero
        # We have one extra row and column, which basically handles if the ending letters in the string match (i.e. our last letters need a base case of 0 to increment from)
        dp = [[0 for j in range(len(text2)+1)] for i in range(len(text1)+1)]
        
        # We will basically fill this story from bottom up
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                # If the character at these index values match, set it to 1 + the grid spot diagonally to the bottom right
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j +1]
                # Otherwise, just carry the currently max stored value, either to the right or below the current location
                else:
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])
        # Return the value that propogated all the way up to the index.
        return dp[0][0]