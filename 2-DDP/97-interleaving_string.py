class Solution:
    """
    Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.
    An interleaving of two strings s and t is a configuration where s and t are divided into n and m substrings respectively, such that:
        - s = s1 + s2 + ... + sn
        - t = t1 + t2 + ... + tm
        - |n - m| <= 1
        - The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
    Note: a + b is the concatenation of strings a and b.
    """
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # Dynamic programming will result in O(m*n) time complexity
        # Base Case
        if len(s1) + len(s2) != len(s3):
            return False
        # Create our dynamic programming table, where s2 letters line up with columns, and s1 lines up with rows, with one extra row and column for the base cases
        # For each i, j, we compare whether s3[i+j] is equal to the value of either i in s1 or j in s2, 
        # and whether a valid interleaving has been produced so far by check to the right of s1 and below s2
        # It should be false, because at this point, if you have zero characters from one string, and n characters from another string, that shouldn't be valid
        dp = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)]
        # set the bottom right value to True, since zero characters from both strings is a valid matching
        dp[len(s1)][len(s2)] = True
        # Go through each grid
        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                # If i or j is not in the "base case null character" row or col, 
                # if either is equal to the i+j'th char in s3, 
                # and if a previous ordering from the previous chars of i and j are possible, set it to true
                # Turning into if-elif seems like it's negligibly faster in test cases, bombed in all cases
                # Putting previous dp value before character check seems to be decent speed up, makes sense
                if i < len(s1) and dp[i + 1][j] and s1[i] == s3[i + j]:
                    dp[i][j] = True
                if j < len(s2) and dp[i][j + 1] and s2[j] == s3[i + j]:
                    dp[i][j] = True
        # Return the top right value
        return dp[0][0]