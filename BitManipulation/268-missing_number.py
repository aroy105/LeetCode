class Solution:
    """Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array."""
    def missingNumber(self, nums: List[int]) -> int:
        # Solution 1:
        # We could use hashing to solve this, and that would use O(n) memory as well
        # Solution 2:
        # However, we could use binary properties to solve this in O(1) memory
        # When we XOR a number by itself, we get 0, and remember this is a commutative operation
        # If we took the XOR of nums and the numbers from 0 to n, we'd be left with the answer. 
        # Solution 3: 
        # If we took the sum of every number from 0 to n inclusive, and we subtracted every number in nums from this list, we'd be left with the number that is missing in nums. 
        # Ex: full_nums = [0, 1, 2, 3, 4], nums = [0, 1, 2, 4]. sum(full_nums) - sum(nums) = (4-4)+3+(2-2)+(1-1)+(0-0) = 3
        
        # Note that to access every value in nums, we have to use i = 0 to len(nums) - 1
        # These numbers of i are also every number in full_nums, excluding n
        # Thus, 'i' can serve a dual purpose in our function, as both a value in full_nums, and the index in nums. 
        # Since addition and subtraction are commutative, we can pretend that for each iteration, we subtract one of the numbers in full_nums from it's corresponding value in nums
        # However, we only have i from 0 to n - 1. We can make sure we check all numbers in 0 to n by just setting our running_result to n. 
        res = len(nums)
        
        # Then, go from every number in 0 to n-1, and append i - nums[i] to our result. Then return the result.
        for i in range(len(nums)):
            res += i - nums[i]
        return res