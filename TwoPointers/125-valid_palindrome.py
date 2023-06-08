class Solution:
    """
    Given a string s, return true if it is a palindrome, or false otherwise.
    We need to convert all letters to lowercase and remove all non-alphanumeric characters before evaluating if it is a palindrome. 
    """
    def isPalindrome(self, s: str) -> bool:
        # Create the left and right pointer at the ends of the string
        l, r = 0, len(s) - 1
        # We'll evaluate until the pointers cross over
        while l < r:
            # From the left, skip over alphanumeric characters
            while l < r and not self.alphanum(s[l]):
                l += 1
            # From the right, skip over alphanumeric characters
            while l < r and not self.alphanum(s[r]):
                r -= 1
            # At this point, we can compare the first starting and ending characters
            # Immediately return false if these characters don't match
            if s[l].lower() != s[r].lower():
                return False
            # If the characters are equal, move both pointers 1 character closer to the center
            l += 1
            r -= 1
        
        # Once all the while loops are done, we should have both pointers either equal or crossed over each other
        # That means we found no paired up characters that weren't equal
        return True
        
    
    def alphanum(self, c):
        """This is what we'll use to determine if the character is alphanumeric"""
        return (
            ord("A") <= ord(c) <= ord("Z") 
            or ord("a") <= ord(c) <= ord("z")
            or ord("0") <= ord(c) <= ord("9")
        )