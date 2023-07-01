class Solution:
    """
    Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

    [4,5,6,7,0,1,2] if it was rotated 4 times.
    [0,1,2,4,5,6,7] if it was rotated 7 times.
    Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

    Given the sorted rotated array nums of unique elements, return the minimum element of this array.
    You must write an algorithm that runs in O(log n) time.
    """
    def findMin(self, nums: List[int]) -> int:
        # While naive solutions generally involve looking for the pivot, consider it this way
        # When we have this kind of a list, we have a sorted portion to the left and right of the pivot. 
        # If we are in the left sorted portion, we want to jump to the right sorted portion instead, where the solution exists
        # Note every value in the left sorted portion > every value in the right sorted portion, 
        # Thus, a simple check to see if we are in the left portion is to check nums[m] >= nums[l].
        
        start , end = 0 ,len(nums) - 1 
        curr_min = float("inf")
        
        while start  <  end :
            mid = (start + end ) // 2
            # determine and store if we have a smaller number
            curr_min = min(curr_min, nums[mid])
            
            # If the mid point is greater than the number at the end, the mid must be in the left sorted portion, so move to the right
            if nums[mid] > nums[end]:
                start = mid + 1
                
            # If the mid point is less than the number at the beginning, the mid must be in the right sorted portion, so keep pushing left to find the minimum such value
            else:
                end = mid - 1 
        
        # At this point, start and end may have converged on a minimum, so just check the value        
        
        return min(curr_min, nums[start])