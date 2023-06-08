class Solution:
    """
    Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. 
    Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.
    Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
    The tests are generated such that there is exactly one solution. You may not use the same element twice.
    Your solution must use only constant extra space.
    These are also 1-indexed, not 0-indexed
    """
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # The brute force intuition is that if we start from the beginning, we can check all elements that are lte the target sum
        # Obviously return if the elements equal target. 
        # Since the list is already sorted in non-decreasing order, if we have found a sum s.t. sum > target, we can ignore everything past our right most element
        # This is because there is now now way it can combine to equal a target, since we just evaluated it with the smallest number possible. 
        
        # Now what if we used a left and right pointer? 
        # If l + r > target, we need to decrement the right pointer and use a smaller value
        # If l + r < target, we need to increment the left pointer and use a larger value
        
        # initialize pointers
        l, r = 0, len(numbers) - 1
        
        while l < r:
            currentSum = numbers[l] + numbers[r]
            
            if currentSum > target:
                r -= 1
            if currentSum < target:
                l += 1
            else:
                return [l + 1, r + 1] # Since it is 1-indexed
        