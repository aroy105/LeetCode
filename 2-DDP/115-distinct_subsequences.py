class Solution:
    """
    Given two strings s and t, return the number of distinct subsequences of s which equals t.
    The test cases are generated so that the answer fits on a 32-bit signed integer.
    """
    # This solution is really slow and really inefficient
    # Look for better answers
    def numDistinct(self, s: str, t: str) -> int:
        # We have a few rules that we can use for solving this types of problem
        # We will have a grid of len(s) + 1 and len(t) + 1, where we will propagate the number of distinct subsequences of s upwards
        # We can imagine the row is all the characters of s1 + "", representing selecting none of the chars, and the other is similarly s1 + ""
        # This is where we will store results to avoid repeated work
        cache = {}
        
        # There were DP problems where we kept an extra row and column at the end, which was kind of like a base case
        # That's what we do over here. If t = "", there's only one combo of s which yields t, which is selecting nothing
        # If s = "", then unless t = "", no combos of it can equal some string t. 
        # Thus, the following lines return 1 for all chars in s where t = "", including when s = "", and return 0 for all chars of t when s = "", except when t = ""
        for i in range(len(s) + 1):
            cache[(i, len(t))] = 1
        for j in range(len(t)):
            cache[(len(s), j)] = 0
        
        # Now, let's iterate through our "rows" and "columns" (we technically don't have a grid), starting from the grid where the end of s and end of t intersect
        # We do this since we just filled the last row and column above
        for i in range(len(s) - 1, -1, -1):
            for j in range(len(t) - 1, -1, -1):
                # If the values match, we have two possible solutions which may be valid
                # The first is where we just increment both the i and j pointed, since the values match
                # But s can be bigger than t, and there may be a future value that matches, so we need to see if a subsequence can be made from using the latter value too
                # i.e. s = hugg, t = hug. At i = j = 2, we can also get a combo by using the i = 3, since the last "g" in s could also match up with the last "g" in t. 
                if s[i] == t[j]:
                    cache[(i, j)] = cache[(i + 1, j + 1)] + cache[(i + 1, j)]
                # Otherwise, the current value at s doesn't pair up with our desired value at t, so just increment it one spot
                else:
                    cache[(i, j)] = cache[(i + 1, j)]
        # At this point, our answer has accumulated at the upper left corner of the grid.
        return cache[(0, 0)]