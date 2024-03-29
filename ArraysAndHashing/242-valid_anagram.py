class Solution:
    '''Given two strings s and t, return true if t is an anagram of s, and false otherwise.'''
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): # Base Case
            return False

        countS, countT = {}, {}

        for i in range(len(s)): # Iterate through each character, increment for each character
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT # Determine if identical hashmaps are generated 