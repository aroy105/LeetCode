class Solution:
    """
    Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

    In other words, return true if one of s1's permutations is the substring of s2.
    """
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # We can have two hashmaps, with keys a-z, for both s1 and the window in s2. Our window in s2 will be as long as the length of s1
        # If the # of a's in s1 match up with the # of a's in the window, we consider this one matching. If both values are 0, this is still a matching (0 == 0)
        # Thus, when we have 26 matching i.e. all characters match up, we have found our permutation, and can break + return true. 
        
        # clear base case
        if len(s1) > len(s2): return False
        
        s1Count, s2Count = [0] * 26, [0] * 26 # Can also use hashmaps instead of lists, but doesn't really matter. This sets all values to 0 initially
        
        # We only need to go through the s1 chars once to 'set' all the initial matchings.
        # This prevents the O(26n) runtime when we go back and try to decrement stuff. 

        for i in range(len(s1)):
            # Go through both s1 and the first window frame of length s1 in s2, and increment these first values. 
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        
        # At this point our data structures have the counts for each char in the alphabet
        
        # Now we count all the matches
        matches = 0
        for i in range(26):
            matches += 1 if s1Count[i] == s2Count[i] else 0
        
        l = 0 
        for r in range(len(s1), len(s2)): # Our right end of the sliding window starts directly after our first window, and goes all the way to the end of s2
            if matches == 26:
                return True
            
            index = ord(s2[r]) - ord('a') # For the character at the current right side of the window, figure out the index it would correspond to in our alphabet "hashmaps"
            s2Count[index] += 1 # Since we've just added the character at the right side of the window, increment it in the window alphabet "hashmap"
            
            if s1Count[index] == s2Count[index]: # If the number of this char in the window now matches the number of that char in s1, our matches just went up by 1
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]: # If we used to have a matching for this character, this new extra right character just caused a mismatch
                matches -= 1
            
            index = ord(s2[l]) - ord('a') # Now do the same for the left side of our window
            s2Count[index] -= 1 # Since this left side character has just been removed from the window, decrement it in the alphabet "hashmap"
            
            if s1Count[index] == s2Count[index]: # If this new change resulted in a matching, increment matches by 1
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]: # If we used to have a matching with that left value, and now it has been removed, we have one less matching
                matches -= 1
            
            l += 1 # Move the window one space to the left
        
        # After our sliding window reaches the end of s2, see if our matches == 26. 
        return matches == 26
            