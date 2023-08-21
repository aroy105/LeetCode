class Solution:
    """Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence. Must be O(n)"""
    def longestConsecutive(self, nums: List[int]) -> int:
        # The naive solution is to sort your numbers, then in one pass, you can check the longest substring. However this is O(nlog(n)) due to merge sort complexity

        # if we visualize the problem, we (the NeetCode guy lol) places all the blocks of sequences on a number line. 
        # To identify the beginning of a sequence, you'll notice the leftmost value has no left neighbor 

        # To check whether the immediate neighbors of a certain value exist, we could just place all our numbers into a set
        numSet = set(nums)
        longest = 0

        # If number - 1 doesn't exist in the set (can now be checked in O(1) time), we know we have the start of a sequence. 
        # If it does exist, we just move to the next value. 
        # If number + 1 exists, we found the next number in our sequence. We continue iterating until number + 1 doesn't exist. 
        for n in nums:
            if (n-1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        # Once we've gone through the array, we should have the longest length
        return longest 