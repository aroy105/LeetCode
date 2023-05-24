class Solution:
    """Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target."""
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for i, n in enumerate(nums):
            diff = target - n # For each element, calculate the difference between the desired value and our value
            if diff in prevMap: # If this difference exists 
                return [prevMap[diff], i] # Return the index and the current index
            prevMap[n] = i  # Key: the number, value: the index