class Solution:
    """
    Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
    The solution set must not contain duplicate subsets. Return the solution in any order.
    """
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # The time complexity will be the number of subsets multiplied by the max length of the subsets, or n*2^n
        # The naive solution (which leads to overcounting) would have the decision points be s.t.:
        # x_1 is on one side, that instance of x_1 can't appear in the other branch. 
        # To avoid duplicates, we need to have it so that if a decision branch is formed, all instances of an integer,
        # even duplicates, are on one side. 
        res = []
        # We need to make sure the array is actually sorted for this to work lol
        nums.sort()
        
        def backtrack(i, subset):
            # base case when we reach end of nums
            if i == len(nums):
                # Code originally had subset[::]. Had to remember that in python, that signifies [start:stop:count]
                # in other words, can't imagine any differences. 
                res.append(subset[:])
                return

            # Create decision point 
            # In the first branch, add the current value in nums to the subset, and push pointer to next value
            subset.append(nums[i])
            # recursively go down first branch
            backtrack(i + 1, subset)
            # In the second branch, don't include any instance of this value
            subset.pop()
            # to that end, go through the list and skip to the last instance of the value
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            # push the pointer to the new value, and recursively go down second branch
            backtrack(i + 1, subset) 
        
        backtrack(0, [])
        return res