class Solution:
    """
    You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals 
    is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
    Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals
    (merge overlapping intervals if necessary). Return intervals after the insertion.
    """
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        # Go through the intervals
        for i in range(len(intervals)):
            # If the new intervals end point is less than the current intervals's start value...
            if newInterval[1] < intervals[i][0]:
                # Just add the newInterval to the previous values, and return the rest of the intervals appended to the end. 
                # We don't need to go through the rest of the values since every other interval must be greater under the if condition, since the intervals are sorted.
                res.append(newInterval)
                return res + intervals[i:]
            # If the new interval start point is greater than the end point of the current interval
            elif newInterval[0] > intervals[i][1]:
                # Add the current interval to our running result list
                res.append(intervals[i])
            # At this point, there is some overlap between the current interval and the new Interval we want to add
            # Thus, redefine the newInterval we need to add as this larger subset. 
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]), 
                    max(newInterval[1], intervals[i][1])
                ]
        # At this point, we haven't been able to insert the newInterval into our list. 
        # This means it either needed to be placed at the end of the list, or the newInterval has been expanded to include all the ending existing intervals. 
        # In either case, add the newInterval to the end of the list, and we'll have the new result of non-overlapping intervals, including our newInterval segment
        res.append(newInterval)
        return res