class Solution:
    """
    There is an integer array nums sorted in ascending order (with distinct values).
    Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) s.t. the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
    For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
    Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
    You must write an algorithm with O(log n) runtime complexity.
    """
    def search(self, nums: List[int], target: int) -> int:
        # Same left and right sorted concept as previous question (153)
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            # Silly little checks I added
            ##################### 
            if target == nums[l]:
                return l 
            if target == nums[r]:
                return r
            #####################

            # The middle pointer is in the left sorted portion
            if nums[l] <= nums[mid]:
                # The first condition is regular Binary Search. 
                # The second condition involves recognizing that if our target is even lower than the lowest number in our left sorted section, the target must be in the right sorted section. 
                # Thus, we can ignore all values left of and at the midpoint. Which is fundamentally the same condition as what happens in Binary search.
                # logic transfers for all other sections
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # The middle pointer is in the right sorted position
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
        