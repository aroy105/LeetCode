class Solution:
    """
    Given a permutation, find the next permutation. The next permutation of an array of integers is the next lexicographically greater permutation of its integer.
    If no such permutation exists, return the lowest lexicographic permutation possible. 
    """
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Seriously tried this one my own, got kind of there
        # based on the solution a 14th century Indian mathematician developed. 
        # This type of problem is where you can generate all permutations of some numbers in lexicographic order 
        # First, find the farthest most value in the permutation that is smaller than the value to the right of it. 
        # Let's call this index i. This is basically the last "rising step", or the max value of i where nums[i] < nums[i+1]
        # If we never see a rising step, we're at the last permutation i.e. all numbers are decreasing, so just sort and return it
        # Then, find the index closest to the end that is greater than nums[i], or the max value of j where nums[i] < nums[j]
        # We then swap nums[i] and nums[j]. 
        # Then, from newly swapped i+1 to the end, reverse that subarray
        # For example. Consider 13452. i = 2, and j = 3. Swap, so we get 13542. Then, reverse from i = 3 to end. Finally, we get 13524
        
        # See if this rising edge exists
        i = -1
        for x in range(1, len(nums)):
            if nums[x-1] < nums[x]:
                i = x - 1
        # If it doesn't we have the last permutation i.e. values are in reverse order, so just return it in sorted order
        if i == -1:
            nums[:] = nums[::-1]
            return nums

        # Find the largest index which is greater than our last rising edge
        j = i + 1
        for x in range(j+1, len(nums)):
            if nums[x] > nums[i]:
                j = x
        
        # Swap i and j
        nums[i], nums[j] = nums[j], nums[i]
        # Reverse the values from i+1 to n
        nums[i+1:] = nums[i+1:][::-1]
        
        return nums
        


    
            
