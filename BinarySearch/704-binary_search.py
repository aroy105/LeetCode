class Solution:
    """
    Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums.
    If target exists, then return its index. Otherwise, return -1.
    """
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        # Until l and r converge on a target
        while l <= r:
            m = l + ((r-1)//2) # Apparently (l + r) // 2 can lead to overflow
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1