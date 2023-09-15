class Solution:
    """Given a string s, return the longest palindromic substring in s."""
    def longestPalindrome(self, s: str) -> str:
        # We will store our longest substring in res, and it's length
        res = ""
        resLen = 0
        # Go through every letter in the string, and use i as the "center" to check for palindromic substrings
        for i in range(len(s)):
            # We will basically check both even and odd length strings
            # An odd length substring is created by setting both our l and r pointers at the same letter
            # Then as we increment it, we'll have a substring of length 1, then 3, then 5 (i.e. odd length)
            # An even length substring is created by setting l to i and r to i+1.
            # Then as we increment it, we'll have a substring of length 2, then 4, then 6 (i.e even length)
            
            # First, we check odd length substrings
            l, r = i, i
            # While the substring we make is still a palindrome and pointers are in bound
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # Check if the candidate is worth checking i.e. bigger than our longest recorded substring (
                if (r - l + 1) > resLen:
                    # If that's the case, update our current longest recorded substring and it's length
                    res = s[l:r+1]
                    resLen = r - l + 1
                # update our left and right pointers
                l -= 1
                r += 1
            # Now, repeat this process for even length substrings
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
        
        return res
            