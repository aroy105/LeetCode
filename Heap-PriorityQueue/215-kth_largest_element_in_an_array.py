# Solution Sorting
class Solution1:
    """
    Given an integer array nums and an integer k, return the kth largest element in the array.
    Note that it is the kth largest element in the sorted order, not the kth distinct element.
    Can you solve it without sorting?
    """
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Naive solution: Sort, then select kth-index, and check the len(arr) - k th index. Due to sorting, this is nlog(n)
        
        # We can also turn the list into a maxHeap (O(n) time). Then, you need to pop k times, and re-heapifying the list is log(n), so overall is n + klog(n)
        

        nums.sort()
        return nums[len(nums) - k]
    
# However, the best average case algo is Quick select, at O(n). Worst case is O(n^2) though. 
# Essentially, take a random pivot, go through the list, and split the list to either be to the left or to the right of the array. 
# Then, switch the value of the pointer with the value at the left end of the right partition
# The worst case time complexity occurs if the list is in reverse sorted order
# When the pivot == len(nums) - k, we know that all vals at indices lower than it are guaranteed to be less, and all vals at indices greater are guaranteed to be more
# In the average case, the pivot selected is middle of the pack, and thus, we go through n, then n/2, then n/4, which from calculus infinite series, we know is O(2n) or just O(n)

class Solution2:
    def partition(self, nums: List[int], left: int, right: int) -> int:
        # Set the pivot to the right-most value, set the left pointer to the front of our list
        pivot, fill = nums[right], left 
        # Move the left pointer through the list, from left to right
        for i in range(left, right):
            # If the current number is lte to the pivot, 
            if nums[i] <= pivot:
                # Swap the value at the left pointer and the current number
                nums[fill], nums[i] = nums[i], nums[fill]
                # Move the pointer up one
                fill += 1
        # All values to the left of pointer (fill) are lte to the pivot. Now, we have to...
        # Swap the right most value (pivot) with the value at the pointer (fill). 
        nums[fill], nums[right] = nums[right], nums[fill]
        # Return the old pointer/current pivot index
        return fill
    
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k # We'll just make k represent the kth index (i.e. where the kth largest element should be)
        left, right = 0, len(nums) - 1 # Set the left and right pointers
        # Use Two pointers to narrow down the range of values to partition and check
        # Since we are guaranteed to find a solution, this will never break
        while left < right:
            # Find the index of the partition
            pivot = self.partition(nums, left, right)
            # If the pivot index is smaller than k...
            if pivot < k: # rerun partition and exclue all values lower than the pivot
                left = pivot + 1 
            # If the pivot is greater than k
            elif pivot > k:
                right = pivot - 1 # Rerun partition and exclude all values greater than the pivot
            # If the pivot is the kth index, break out of the loop
            else:
                break 
        # Return the value of the kth largest number
        return nums[k]