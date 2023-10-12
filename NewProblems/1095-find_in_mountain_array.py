class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
      """
      You may recall that an array is a mountain array if and only if 
      1) it's length is at least three, and 
      2) there exists i with 0 < i < arr.length - 1 s.t. arr[0] < arr[1] < ... < arr[i - 1] < arr[i] AND arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
      Basically, it looks like a mountain, monotonically increasing to a peak, then monotonically decreasing from the peak
      Given a mountain array, return the minimum index s.t. mountainArr.get(index) == target. If this index doesn't exist, return -1. You can't access this array directly
      You can only use the interface, and make sure you use MountainArray.get less than 101 times. 
      """
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        # First, we find the peak
        # Then, we check the start-to-peak. If we can't find it there, then we check peak-to-end
        # We return this result

        def peak_finder(mountain_arr):
            # We run a type of binary search, whcih is slightly modified
            # We calculate mid, as normal. However, we check the value next to it as well. This allows us to see if we're increasing or decreasing here.
            
            
            left, right = 0, mountain_arr.length() - 1
            while left < right:
                mid = left + (right - left) // 2
                # If this is an increasing section, we set our left bound up to the neighbor next to mid i.e higher neighbor is new min
                if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                    left = mid + 1
                # If it's a decreasing section, we set our right bound down to the mid point i.e. mid is our new max
                else:
                    right = mid
            # Remember, with this implementation, our value falls in left. 
            return left 
        
        
        def binary_search(left, right, is_increasing):
            # This implementation of binary search can be modified for both sides of the peak
            # we regularly run binary search up until...
            while left <= right:
                mid = left + (right - left) // 2
                mid_val = mountain_arr.get(mid)
                # If our new mid_point is equal to our target, return the target
                if mid_val == target:
                    return mid
                # ...here. At the binary checker, we see if we know this section is increasing or decreating. 
                # If mid_value is smaller than our target...
                # and we're increasing, then set our min value (left) directly to the right of mid
                # If we're decreasing at this point, then our min value (right) is instead directly to the left of mid
                if mid_val < target:
                    if is_increasing:
                        left = mid + 1
                    else:
                        right = mid - 1
                # if mid value is larger than or equal to our target...
                # And we're increasing, set our max value (right) directly to the left of mid
                # If we're decreasing instead, set our max value (left) directly to the right of mid
                else:
                    if is_increasing:
                        right = mid - 1
                    else:
                        left = mid + 1
            # if our left and right boundary pointers crossed over but we couldn't find a satisfactory answer, return -1
            return -1 

        # Find our peak
        peak_index = peak_finder(mountain_arr)
        # See if we can find our answer from the start of the mountain to the peak
        result = binary_search(0, peak_index, True)
        # If we couldn't, see if we can find the answer from right after the peak to the end. 
        if result == -1:
            result = binary_search(peak_index + 1, mountain_arr.length() - 1, False)
        # Return our result.
        return result
