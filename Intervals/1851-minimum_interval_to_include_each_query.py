import heapq
class Solution:
    """
    You are given a 2D integer array intervals, where intervals[i] = [lefti, righti] describes the ith interval starting at lefti and ending at righti (inclusive).
    The size of an interval is defined as the number of integers it contains, or more formally righti - lefti + 1.
    You are also given an integer array queries. The answer to the jth query is the size of the smallest interval i such that lefti <= queries[j] <= righti. 
    If no such interval exists, the answer is -1.
    Return an array containing the answers to the queries.
    """
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # We need to sort our list, and we'll also use a minHeap to find smallest intervals, yielding a time complexity of O(nlogn + qlogq)
        intervals.sort()
        minHeap = []
        # We use a dictionary since it may not be sorted
        res = {}
        i = 0 
        # Go through each query 
        for q in sorted(queries):
            # While we haven't exceeded the number of intervals even there, and while the left value of the interval is lte our query...
            while i < len(intervals) and intervals[i][0] <= q:
                # Add the interval to our minheap, we sort by the size of the interval first, then how quickly it terminates (r value)
                # By sorting this way, we follow a greedy approach, and prioritize intervals which wouldn't collide with future intervals
                l, r = intervals[i]
                heapq.heappush(minHeap, (r - l + 1, r))
                # Iterate to move to next interval in sorted list
                i += 1
            # Given the eligible intervals, go though them and if they end before the query, remove them permanently for all future queries. 
            # This ensures that the queries we use in the future are far enough down the number line to contain our later queries
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            # If there are valid intervals at this point, return the top of the minHeap as the result. If not, return -1
            res[q] = minHeap[0][0] if minHeap else -1
        return [res[q] for q in queries] # This helps spit out results in order they were produced in input queries.
                
        