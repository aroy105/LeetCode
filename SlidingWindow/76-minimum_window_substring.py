class Solution:
    """
    Given two strings s and t of lengths m and n respectively, return the minimum window substring
    of s such that every character in t (including duplicates) is included in the window. 
    If there is no such substring, return the empty string "".

    The testcases will be generated such that the answer is unique.
    """
    def minWindow(self, s: str, t: str) -> str:
        # The brute force way is to maintain two hashmpas, where called Have and Need. Have is a window which we are currently examining, Need will be fixed. 
        # As long as all the entries in Have are greater than or equal to the corresponding entries in Need, we have a valid substring. 
        # However, each time we successively expand our window, we need to double check our previous entries to see if Have[prev] == Need[prev]
        # But what if we instead kept track of two variables, H and N. Initially, N is set to the length of t, and H is set to 0, but H is incremented everytime an entry in Have is first == entry in Need
        # When H == N, we know we have found a potential result.
        # However, this isn't necessarily a minimum result, so we can slide the left side index until we don't have a valid substring. Then we repeat this process. 
        
        # Basically, increase the window until we get a valid solution, then decrease until we don't have a valid solution. Repeat until we reach the end of the s. 
        if t == "": return ""
        
        countT, window = {}, {}
        # Create the table for our Need values. 
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        have, need = 0, len(countT) # Create our H and N values
        res, resLen = [-1, -1], float("infinity") # initialize our stored answer
        # Start the sliding window part
        l = 0
        for r in range(len(s)):
            c = s[r] # the character at the right end of the window
            window[c] = 1 + window.get(c, 0) # Add this character to our window hashmap
            
            # if this character is needed in t, and if the current count of this character is the same in both our window and t...
            if c in countT and window[c] == countT[c]:
                have += 1 # One more requirement has been satisfied
            
            # while we have a valid substring...
            while have == need:
                # if this new substring length is less than our previous min length, store this as the new answer
                if (r - l + 1) < resLen:
                    res = [l, r]
                    res = r - l + 1
                
                # Decrease the size of our valid substring by one
                window[s[l]] -= 1
                # If the character we removed was in t and if it wasn't just an excess character (i.e. we needed it for a valid substring)
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    # We now don't have a valid substring, and we must decrease our h counter
                    have -= 1
                # move our window from the left one space over
                l += 1
        # After our whole sliding window, set our window pointers to the stored optimal solution
        l, r = res
        # If we found an optimal solution, return it as a substring of s, and if not, return and empty string. 
        return s[l:r+1] if resLen != float("infinity") else ""
        
                    
        
        
        
        
        