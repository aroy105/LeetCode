class Solution:
    """
    Given array of intervals intervals where intervals[i] = [starti, endi], return min # of intervals to remove to make the rest of the intervals non-overlapping.
    """
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Remember problem doesn't state intervals are sorted, so we need to do that one first
        intervals.sort()
        # We will employ a greedy algorithm to solve this problem. 
        # In general, if there is an overlap, we remove the one that ends later, to avoid possible collisions with future intervals
        res = 0 
        # Create a pointer, and set it at the end value of the first interval
        prevEnd = intervals[0][1]
        # Go through the rest of the intervals...
        for start, end in intervals[1:]:
            # If the current interval's start value is at or after the end of the previous interval, we can just shift the pointer up to the current interval
            if start >= prevEnd:
                prevEnd = end
            # If there is an overlap, we must remove the overlap (res += 1) and then set the pointer to the interval that termiantes earlier.
            else:
                res += 1
                prevEnd = min(end, prevEnd)
        # Return the number of such intervals
        return res
        