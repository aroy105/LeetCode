import heapq
class KthLargest:
    """
    Design a class to find the kth largest element in a stream. Note that it is the kth largest element in sorted order, not the kth distinct element
    Implement this class
    """
    # A stream just means we could continue to add elements to the list and evaluate on a rolling basis
    # We will use a minheap of size k 
    def __init__(self, k: int, nums: List[int]):
        """Initializes the object with the integer k and the stream of integers nums."""
        # Turn our initial data structure into a heap, and set the size of the data structure to be k
        self.minHeap, self.k = nums, k 
        # Turn the input data into a heap
        heapq.heapify(self.minHeap)
        # Reduce the size of the minheap tuntil it is size k
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)
        
        
    def add(self, val: int) -> int:
        """Appends the integer val to the stream and returns the element representing the kth largest element in the stream."""
        heapq.heappush(self.minHeap, val)
        # If we exceeded the space of the minHeap (i.e. added an element that must be lower than kth largest element, pop whatever is now the lowest)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        # Return the top of the heap
        return self.minHeap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)