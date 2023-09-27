class Solution:
    """
    Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:
        - '.' Matches any single character.​​​​
        - '*' Matches zero or more of the preceding element.
    The matching should cover the entire input string (not partial).
    """
    def isMatch(self, s: str, p: str) -> bool:
        # Bottom-Up DP (Slightly faster, more confusing to write)
        # Remember, this checks and stores all cases, and propogates values to the top left from the bottom right
        # We add an extra row and extra column, to represent when we exhaust either the string or the pattern. If pattern is exceeded before string, pattern couldn't match to string, so return False
        cache = [[False] * (len(p) + 1) for i in range(len(s) + 1)]
        # However, if both the string and pattern pointers both exceed the string, we have found a pattern that describes the string, so return True for this case
        cache[len(s)][len(p)] = True
        # Start at the last row and the second to last column i.e. the last char in p and the "" char after the last char in s. This handles cases where we should return True for s = "" p = "a*"
        for i in range(len(s), -1, -1):
            for j in range(len(p) - 1, -1, -1):
                # Determine a match has been created if we are not in the last row (i.e. the "" char after the last char in s) and s[i] can be represented by p[j] either directly or by wildcard char "."
                match = i < len(s) and (s[i] == p[i] or p[j] == ".")
                # If the (j + 1)th pointer isn't right after where p ends, and if it is "*"
                if (j + 1) < len(p) and p[j + 1] == "*":
                    # We first assume no match, so set it to the truth value of the grid if we skipped the "_*" in the pattern. Therefore, we check the next pattern char after the "_*", or two spaces over
                    cache[i][j] = cache[i][j + 2]
                    # If there was a match however, we can just check if the next char in s is equal to the char we're repeating in pattern, or if the current spot is true 
                    # We also have to check cache[i][j]. cache[i][j] is only true if we didn't need the "_*" pattern and it evaluated to true right above
                    # We don't want to overwrite this truth value if the solution where we skip "*" did work, which might happen if cache[i + 1][j] = False
                    if match:
                        cache[i][j] = cache[i + 1][j] or cache[i][j]
                # Otherwise, if [j:j+2] is not "_*", but we have a match at the current spot, just check if our previous subcase where we were one pointer ahead was true
                elif match:
                    cache[i][j] = cache[i + 1][j + 1]
            
        # At this point, value is propogated up to upper left hand corner
        return cache[0][0]
    
    def isMatchTopDown(self, s, p):
        # Top-Down Memoization (Slightly slower, easier to understand/write)
        # This skips cases
        cache = {}
        
        def dfs(i, j):
            # These are our base cases
            # If the configuration of i and j pointers have already been cached, just return the previously saved value
            if (i, j) in cache[(i, j)]:
                return cache[(i, j)]
            # If the pattern has been adequetly described by the string i.e. the i pointer and j pointer have equaled or exceeded the length of the string, return true
            if i >= len(s) and j >= len(p):
                return True
            # If the pattern has been exhausted but the string still has letters, then it failed to describe the string
            if j >= len(p):
                return False
            # Determine if the current values at i and j in s and p are equal or if p can represent s[i]
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")
            # If we haven't reached the end of the pattern string and the pattern indicates a "*" repeated character (i.e. multiple characters can be represented)...
            # At this point, j is the spot of the element that must be repeated, and j + 1 is the * character
            if (j + 1) < len(p) and p[j + 1] == "*":
                # This pairing in the pattern can be true under two conditions, and if either is satisfied, it's true for this subcase
                # Either we use the no-repition option (i.e. we don't use * at all, so we skip both the element we repeat and *, which is j + 2)
                # Or we see there's a match between i and the element we want to repeat, and if the next elements in our string also recursively match the element we must repeat (dfs(i+1, j))
                # The first case is where we may have s[i] = "d" and p[i:i+2] = "c*", so we can select zero instances of d. The second case is s = "ddddd" and p = "d*"
                cache[(i, j)] = dfs(i, j + 2) or (match and dfs(i + 1, j))
                # Return the result for this subcase once we've recursively ran through all the other cases
                return cache[(i, j)]
            # If the current pattern is not "*" and we have a match (s[i] = "x" and p[j] = "x" or "."), increment i, j by one, and recursively check next index. Once recursion ends, store value.
            if match:
                cache[(i, j)] = dfs(i + 1, j + 1)
                return cache[(i, j)]
            # At this point, we didn't have a "_*" pattern, nor did we have a match at the current index. The pattern doesn't match the string, so save this subcase and return false
            cache[(i, j)] = False
            return False 
        # Start the backtracking stuff at the 0th index of both the string and the pattern
        return dfs(0, 0)