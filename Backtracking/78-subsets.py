class Solution:
    """
    Given an integer array nums of unique elements, return all possible subsets (the power set).
    The solution set must not contain duplicate subsets. Return the solution in any order.
    """
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # When we think about a powerset, for each element, we can either include or not include it in the subset. 
        # Thus, there are 2^n elements in a powerset
        
        # What we will do is go down this decision tree, where we choose or don't choose to add certain elements
        res = [] # Place answers here
        subset = []
        
        def dfs(i):
            # Base Case, when we reach end of nums (no more elements/decision points to go down)
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # record two paths now
            # Include nums[i]
            subset.append(nums[i]) # Add it to subset and go to next decision point
            dfs(i + 1)
            # Exclude nums[i] 
            subset.pop() # Remove it from working subset and go to next decision point
            dfs(i + 1)
        
        dfs(0)
        return res