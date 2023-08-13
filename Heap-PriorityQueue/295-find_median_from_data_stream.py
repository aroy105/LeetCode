import heapq
class MedianFinder:
    """
    The median is the middle value in an ordered integer list. 
    If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.
    """
    # The idea is we make a small Heap and a Big Heap, and both heap sizes don't differ by more than one. 
    # All values in the small heap are lte to all values in the big heap. 
    # That way adding and removing an element is always a log(n) operation
    def __init__(self):
        """initializes the MedianFinder object."""
        # initialize the maxHeap and the minHeap
        self.small, self.large = [], [] 

    def addNum(self, num: int) -> None:
        """adds the integer num from the data stream to the data structure."""
        # If len(large heap) > 0, and num > min value in large heap, add it to the small heap
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        # Otherwise, add it to the small heap. Remember the small heap is a maxHeap, so multiply by -1
        else:
            heapq.heappush(self.small, -1*num)
        
        # If small heap is greater than the large heap by more than one...
        if len(self.small) > len(self.large) + 1:
            # add largest value in small heap to large heap
            val = -1*heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        # If large heap is greater than the small heap by more than one...
        if len(self.large) > len(self.small) + 1:
            # add smallest value in large heap to small heap
            val = -1*heapq.heappop(self.large)
            heapq.heappush(self.small, val)

    def findMedian(self) -> float:
        """returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted."""
        if len(self.small) > len(self.large):
            return -1*self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        return (-1*self.small[0] + self.large[0])/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()