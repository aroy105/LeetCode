class Solution:
    """
    Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
    Notice that the solution set must not contain duplicate triplets.
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # This problem is an interesting combination of the Two Sum Problems, where we have a + b + c = target
        # Basically, if we sort the list, we can just do Two Sum II n times by fixing our current index as a, and then finding b and c that equal target - a
        # We can also avoid duplicates via sorting by just skipping values for a that we have already checked 
        res = []
        nums.sort()
        
        for i, a in enumerate(nums):
            # If this isn't the first value in the input array (i > 0) and current a == previous a
            if i > 0 and a == nums[i - 1]:
                continue # Go to the next index for a
            # Now basically do Two Sum II
            l, r = i + 1, len(nums) - 1 # nums[l] is b and nums[r] is c, or our front and back pointers for Two Sum II
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    # Now we need to update our pointers, and this part gets a little tricky. 
                    # We technically only need to update one of the pointers, and the above code will handle incrementing or decrementing the other
                    l += 1
                    # If we have the same value for l repeatedly coming up, we should save ourselves some time and push it to the next unique value (but not over the right pointer)
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res