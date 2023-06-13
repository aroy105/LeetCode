class Solution:
    """
    You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. 
    You can perform this operation at most k times.
    Return the length of the longest substring containing the same letter you can get after performing the above operations.
    """
    def characterReplacement(self, s: str, k: int) -> int:
        # When deciding characters to replace in a substring, always opt for the characters which are less frequent
        # If we maintain a hashmap, we can count the number of chars for each char
        count = {}
        res = 0 
        l = 0
        # Then, in some substring created by a sliding window, if the windowLength - count[mostFreqChar] <= k, our window is valid
        # When this condition is broken, we need to push the left end of the sliding window until the window becomes valid again. 
        # As we make push the left window, we need to decrement the count of chars in the hashmap
        # If we did this naive solution, we'd have a O(26n) solution, but there's a little trick we can use
        # Technically, the maxFreq doesn't need to ever be decremented. 
        # If the length of our substring increases, as new characters get introduced, our maxFreq would also either go back to the same value, or be replaced by a new dominant char
        # Think about this last line carefully. NeetCode guy said this realization isn't really necessary for most interviews, and O(26n) solution is fine. 
        maxf = 0 
        for r in range(len(s)): # Right sliding window
            count[s[r]] = 1 + count.get(s[r], 0) # Add the right window char to the hashmap
            maxf = max(maxf, count[s[r]]) # Update our max frequency variable if needed
            
            # This step will be skipped if the window is valid. If skipped, the window will continue to increase in size. 
            if (r - l + 1) - maxf > k: # Our Window is not valid
                # Update left side of window
                count[s[l]] -= 1
                l += 1
                # These two steps will make sure the window will only maintain the size of the largest valid substring. Note, this step does not decrease the window.
            
            # If our window is valid and also increased, the longest recorded length will increase to match the window size. 
            res = max(res, r - l + 1)
        
        return res
            
        
        