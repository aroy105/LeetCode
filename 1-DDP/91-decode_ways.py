class Solution:
    """
    A message containing letters A-Z can be encoded by mapping A to 1, B to 2, ..., Z to 26. 
    To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). 
    For example, "11106" can be mapped into: "AAJF" with the grouping (1 1 10 6) and "KJF" with the grouping (11 10 6) 
    Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".
    Given a string s containing only digits, return the number of ways to decode it.
    The test cases are generated so that the answer fits in a 32-bit integer.
    """
    def numDecodings(self, s: str) -> int:
        pass