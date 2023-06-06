class Solution:
    """
    Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
    If there is no future day for which this is possible, keep answer[i] == 0 instead.
    """
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # A brute force approach would be quick and dirty, and also O(n^2)...
        # One trick we can use is we can use a stack to store values until we find a higher one
        # When we find a higher value, we can just pop all lower values sequentially
        # Our stack will be in monotonic decreasing order
        res = [0]*len(temperatures)
        stack = []
        
        for i, t in enumerate(temperatures):
            # While stack is nonzero and our latest t is greater than the top value in the stack...
            while stack and t > stack[-1][0]:
                _, stackInd = stack.pop()
                # The result value for the particular day will then be the difference between the index of the current high (i) and the lower temp day (stackInd)
                res[stackInd] = (i - stackInd)
            # Add the high temp day to the stack
            stack.append([t, i])
    
        return res