class Solution:
    """
    Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
    The overall run time complexity should be O(log (m+n)).
    """
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Basically, we try to correct left partitions for nums1 and nums2, and find the median from there
        
        # Set A and B to be the larger and smaller list respectively
        A, B = nums1, nums2
        if len(B) < len(A):
            A, B = B, A
        
        total = len(nums1) + len(nums2)
        half = total // 2
        
        # Do binary search on A
        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2 # midpoint for A
            # To calculate the midpoint for B, let's think about it
            # From 0 to i, we have assumed these values will be in the left partition
            # We know the total possible values that can be in the left partition are total//2 = half. 
            # So to calculate the remaining values that can be allocated from B to the left partition, we need to to half - i
            # However, i is an index, and doesn't represent the actual number of values from A in the partition. We need to subtract 1 since indices are 0-indexed. 
            # Respectively, j is also an index, and thus is zero indexed. So we need to subtract another 1.
            j = half - i - 1 - 1 # midpoint for B
            
            # Now we have to compare the values in the left and right partitions to see if we have a correct partitioning scheme
            # However, edge cases need to be handled when these pointers are potentially at the edges of nums1 and nums2
            
            # represents number at the right edge of left partition for both lists
            Aleft = A[i] if i >= 0 else float("-infinity") 
            Bleft = B[j] if j >= 0 else float("-infinity")
            # represents number at the left edge of right partition for both lists
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity") 
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")
            
            # If our left partition edge values in both lists are lte than the right partition edge values in the opposite list i.e. we have a correct partition...
            # Think carefully, if largest value in left partition of B is lte smallest value in right partition of A, and vice versa, our partition is valid
            if Aleft <= Bright and Bleft <= Aright:
                # if our list number is odd, collect traditional median
                if total % 2:
                    # Imagine our arrays are merged and sorted. If we took all elements from 0 to Aleft and Bleft respectively, we have the entirety of the left partition
                    # Thus, the next number would be the median if len(list) is odd. Since it is sorted, you'd take the smaller of the numbers to get this value 
                    return min(Aright, Bright)
                # At this point, list must be even, so take the two numbers closest to the middle
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            # If the largest value in the left partition of A is greater than the smallest value in the right partition of B i.e. A's contributing left partition is too large...
            elif Aleft > Bright:
                r = i - 1 # Reduce the size of the left partition from A
            # If instead B is now contributing too many elements to the left partition... 
            # (Reminder this just means that we included a value from B in the left partition that should be in the right partition)
            else:
                l = i + 1 # Increase the size of the left partition from A
                
        
        