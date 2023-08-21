class Solution:
    """
    Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
    and return an array of the non-overlapping intervals that cover all the intervals in the input.
    """
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Remember problem doesn't state intervals are sorted, so we need to do that one first
        intervals.sort(key=lambda pair: pair[0])
        output = [intervals[0]]
        
        # For each start and end pair in intervals...
        for start, end in intervals:
            # Grab the previous interval's end value
            lastEnd = output[-1][1]
            # If current interval's start value is <= previous interval's end value, expand the previous interval to be previous + current interval
            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end) # Take the previous interval, and reset the end value to the current interval's end value
            # If the current interval is completely after the previous interval
            else:
                output.append([start, end])
        return output
                
            