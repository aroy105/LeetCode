class Solution:
    """
    Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
    Note that the same word in the dictionary may be reused multiple times in the segmentation.
    """
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # This stores a list of indices and whether or not there is a possible word break at that location
        dp = [False] * (len(s) + 1)
        # Naturally, there is a wordbreak at the end
        dp[len(s)] = True 
        # We take a bottom up approach
        for i in range(len(s) - 1, -1, -1):
            # We go through every word in our dictionary
            for w in wordDict:
                # If the index + the size of the word is lte the size of the words (i.e. in bounds) and the string from the index to the index + size of word == word
                if (i + len(w)) <= len(s) and s[i: i + len(w)] == w:
                    # Set the truth value of the current index to the truthiness of the previous wordbreak (Which should be true)
                    dp[i] = dp[i + len(w)]
                # If the current index is already true, we can break, and decrement one letter
                if dp[i]:
                    break
        # Return the truthiness at the index. True indicates that s was able to be turned into a sentence with the words in the dictionary
        return dp[0]