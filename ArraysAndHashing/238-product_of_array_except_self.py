class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i]."""
        # For any i in the nums, it would be helpful to know what the products are for both elements < i and elements > i
        # We can call these values the prefix and postfix values, and multiplying these two gives the answer

        # It would be easy to just make arrays for prefix and postfix values. Just multiply the first number in the sequence with the next term, or vice versa for postfix values
        # In one pass, the entire arrays could be populated

        # Then, for each i, just find the prefix at i - 1 and postfix at i + 1, and multiply these values. If you go past the bounds of the array, this value is basically just 1.

        # A more intelligent system can be construced where instead of having the extra memory, just store the prefixes into the output array, shifted to the left by one space
        # Now that all the prefixes are already stored in the output array, multiply the value in each spot by the postfix value, starting from the right. 

        # Thus, in two passes, the problem is solved. 

        res = [1] * (len(nums)) # Instead of doing zero, multiply by one, since this is the default value of the first position in the array
        
        prefix = 1 
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res

