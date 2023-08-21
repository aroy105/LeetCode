class Solution(object):
    """Given array of meeting time intervals consisting of start and end times[[s1,e1],[s2,e2],...](si< ei), find the minimum number of conference rooms required."""
    def minMeetingRooms(self, intervals):
        # To see how many rooms are needed, go through each point in time, and see how many concurrent meetings there are. 
        # This way, the max number of concurrent meetings is the number of rooms needed. NeetCode figured this out via drawing
        
        # Sort the start and end times
        time = []
        # Add start/end times as tuples. Denote start times as 1, and end times as -1
        for start, end in intervals:
            time.append((start, 1))
            time.append((end, -1))
        # Sort times first by actual time, then by whether it is a start or end time
        time.sort(keys=lambda x: (x[0], x[1]))
        
        # Initialize counters
        count = 0
        max_count = 0 
        # Go through each time tick
        for t in time:
            # Add to the count if a meeting starts at this tick mark
            # Subtract to the count if a meeting ends at this tick mark
            # Remember, t[1] stores whether a meeting starts (+1) or ends (-1)
            count += t[1]
            # Update the max count
            max_count = max(max_count, count)
        return max_count