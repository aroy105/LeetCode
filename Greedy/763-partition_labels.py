class Solution:
    """
    You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.
    Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.
    Return a list of integers representing the size of these parts.
    """
    def partitionLabels(self, s: str) -> List[int]:
        # Create a dictionary to store the last instance of each letter
        count = {}
        res = []
        
        i, length = 0, len(s)
        # Go through every character in the string, and add it to the count dictionary
        for j in range(length):
            c = s[j]
            count[c] = j
        # Keep track of the size of the current segment, along with the goal length
        curLen, goal = 0, 0
        # While we haven't reached the end of the list....
        while i < length:
            # Get the character
            c = s[i]
            # If this character's last instance is beyond the current goal length, push the goal length up to encompass all instances of that character too.
            goal = max(goal, count[c])
            # Update the size
            curLen += 1
            # If the index reaches goal, we have created our first successful segment, so add the size of the segment to results.
            if goal == i:
                res.append(curLen)
                curLen = 0
            # Move to the next character
            i += 1
        return res
        