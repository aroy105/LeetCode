class Solution:
    '''Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.'''
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set() # Create a hashset for O(1) indexing
        for n in nums: # Iterate through every element in the list
            if n in hashset: # If a duplicate is found return true
                return True
            hashset.add(n) # Else add it to the hash set
        return False # If we reach this point, no duplicates can exist.