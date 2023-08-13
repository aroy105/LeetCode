class Solution:
    """Given array of meeting time intervals consisting of start & end times [[s1,e1],[s2,e2],...] (si < ei), check if a person could attend all meetings."""
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda i: i[0]) # Sort by first element
        # Go through every meeting from the second meeting to the end
        for i in range(1, len(intervals)):
            # Get the previous meeting details
            i1 = intervals[i - 1]
            # Get the current meeting details
            i2 = intervals[i]
            # If the previous meeting ends after the current meeting begins, return False
            if i1[1] > i2[0]:
                return False 
        # At this point, no time conflicts have been found. 
        return True