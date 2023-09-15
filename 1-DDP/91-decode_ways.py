class Solution:
    """
    A message containing letters A-Z can be encoded by mapping A to 1, B to 2, ..., Z to 26. 
    To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). 
    For example, "11106" can be mapped into: "AAJF" with the grouping (1 1 10 6) and "KJF" with the grouping (11 10 6) 
    Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".
    Given a string s containing only digits, return the number of ways to decode it.
    The test cases are generated so that the answer fits in a 32-bit integer.
    """
    def numDecodingsMemoizationApproach(self, s: str) -> int:
        # Memoization (O(n) time and memory, recursive caching solution)
        # Base Case: If we get an empty string, there is always 1 way to return the answer
        dp = {len(s): 1}
        # i will be the positiion we are at in our string
        def dfs(i):
            # If i has been cached already, or if we reach the end of the string (len(s): 1), return the cached value
            if i in dp:
                return dp[i] 
            # This is a bad base case, if our string starts with zero, this is an invalid mapping. 
            if s[i] == "0":
                return 0
            # Now, we use recursion. 
            # At this point, we have either established that this particular grouping starting at i hasn't been checked, and this grouping isn't invalid by starting with 0.
            # There are two cases from which we recursively check all groupings. That is where we go forward with EITHER (i+1) OR (i+1, i+2)
            # We already have checking to see if the single unit grouping is valid (look at the above two base cases), so just recursively check it
            res = dfs(i + 1)
            # Now at this point, res has the number of groupings if we had gone with a single (i+1) grouping.
            # We now check if the (i+1, i+2) grouping is valid
            # If the next index is still less than the length of the string, 
            # AND if (i+1, i+2) grouping starts with 1 (i.e. it's letter 10-19), OR the (i+1, i+2) grouping starts with 2 and ends with 0-6 (i.e. it's letter 20-26)
            if i + 1 < len(s) and (
                s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"
            ):
                # Add the total future groupings from considering (i+1, i+2)
                res += dfs(i + 2)
            # Since our base cases established that this # of groupings wasn't cached, add it to our cache, and kick the result up the recursion chain
            dp[i] = res
            return res
        # Return the total number of groupings, starting from the beginning index.
        return dfs(0)

    def numDecodingsDPApproach(self, s: str) -> int:
        # Base case where len(s) == 0 (i.e. only one possible grouping) or we reached the end of the string (i.e. only one way to group from that index)
        dp = {len(s): 1}
        # Starting from the last index to the beginning index...
        for i in range(len(s) - 1, -1, -1):
            # No grouping can start with 0 i.e. (0) or (0 X) will always be invalid
            # If the value at the index is 0, all decoding schemes using this are not usable, so store the groupings at this index as 0
            if s[i] == "0":
                dp[i] = 0
            # If it is non zero, the groupings are at least the total groupings from the index we were just at
            else:
                dp[i] = dp[i + 1]
            # If this index and the index we were just at can create a valid combination, we have another valid combo.
            # Therefore, we need to consider all the other future groupings again, since that x2 the number of combos thus far. 
            # To properly count the combos, consider everything that starts from after a new two-digit grouping, and add it to our running count for this index
            if i + 1 < len(s) and (
                s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"
            ):
                dp[i] += dp[i + 2]
        # The accumulated values are now stored at the 0th index in our dictionary. 
        return dp[0]
        
                
            
        