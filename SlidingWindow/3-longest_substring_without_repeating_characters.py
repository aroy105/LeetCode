class Solution:
    """Given a string s, find the length of the longest substring without repeating characters."""
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set() # Store all the characters in a set
        l = 0 # left side of sliding window
        res = 0
        
        for r in range(len(s)): # right side of sliding window
            # In while loop, we've reached chars that are repeating
            while s[r] in charSet:
                # Update the left side of the sliding window
                charSet.remove(s[l]) 
                l += 1 
            # At this point, we've pushed the left end of the sliding window until we have a substring with only unique characters
            charSet.add(s[r]) # Add the right end of the sliding window to the charSet 
            res = max(res, r - l + 1) # Check the length of our new substring
        
        return res
        