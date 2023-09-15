class Solution:
    """
    Given a string s, return the number of palindromic substrings in it.
    A string is a palindrome when it reads the same backward as forward.
    A substring is a contiguous sequence of characters within the string.
    """
    def countSubstrings(self, s: str) -> int:
        res = 0
        # For each letter
        for i in range(s):
            # Calculate the # of palindromic substrings where i or i/i+1 is the center
            # If I am confused, reference Problem #5 for rationale here
            res += self.countPalindromes(s, i, i) # Odd-length substrings
            res += self.countPalindromes(s, i, i+1) # Even-length substrings
        return res
    
    def countPalindromes(self, s, l, r):
        # This will count the number of palindromes given the string and starting left and right pointers
        res = 0
        # While the pointers are in bound and the substring is a palindrome
        while l >= 0 and r < len(s) and s[l] == s[r]:
            # We found a palindromic substring, so update the result count
            res += 1
            # Increment pointers
            l -= 1
            r += 1
        return res