class Solution:
    """
    You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.
    
    Return the maximum possible length of s.
    """
    def maxLength(self, arr: List[str]) -> int:
        dp = [set()]
        for string in arr:
            # Skip strings that use duplicate letters, since this can't be used in answer
            if len(set(string)) < len(string): continue
            string = set(string)
            # This is a shallow copy of dp, that won't get modified. 
            # We will slowly add combos that include the first string.
            # The outer loop will ensure that with the next string, we check it against all exsting combos, and so on
            for combo in dp[:]:
                # Find what is in both the string and the combo. If there's something, go to the next combo
                if string & combo: continue
                # Add this new combination to the set.
                dp.append(string | combo)
        # Return the biggest number out of the lengths of each string.
        return max(len(string) for string in dp)
