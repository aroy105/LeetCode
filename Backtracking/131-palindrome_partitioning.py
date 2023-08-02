class Solution:
    """
    Given a string s, partition s so that every substring of the partition is a palindrome. 
    Return all possible palindrome partitioning of s. 
    """
    def partition(self, s: str) -> List[List[str]]:
        # Notice that there is always at least one way to partition the word (split every single letter into a partition, a single letter is a palindrome)
        res = []
        # Store our current partitions 
        part = []
        
        def dfs(i):
            # Reached end of remaining string in recursive call
            if i >= len(s):
                res.append(part[:])
                return 
            # Go through every possible substring
            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    # Store valid partition
                    part.append(s[i : j + 1])
                    # This bit is kind of weird. Basically, this shifts i up one, and the next recursive call's for loop goes from i + 1 to the end. 
                    # This way, we check every single substring. This increases time complexity, since we now check substrings starting from i + 1, i + 2, etc
                    dfs(j + 1)
                    # Recursive unwinding
                    part.pop()
        dfs(0)
        return res 
    
    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False 
            l, r = l + 1, r - 1
        return True