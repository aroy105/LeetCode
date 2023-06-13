import collections
class Solution:
    """
    You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. 
    You can only see the k numbers in the window. Each time the sliding window moves right by one position.

    Return the max sliding window.
    """
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # The naive solution would be for each sliding window we have, just iterate through it, and add the max value to some kinda list. However, this will be O(k*(n-k))
        # However, we can optimize this a little. Essentially, if we have a window where there is some x greater than all previous values, we can disregard the previous values
        # We can use a deque, and in our deque, we'll always have values in decreasing order. As a new higher value comes in, we can pop off all lesser values
        output = []
        q = collections.deque() # This will contain indices
        l = r = 0
        # While the right side of our sliding window has not reached the end of the array...
        while r < len(nums):
            # Remove all values smaller than r in the queue
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            # Add the right most element in our window to the queue
            q.append(r)

            # OK THIS PART TRIPPED ME UP BECAUSE I WAS STUPID
            # BASICALLY, l IS OUR CURRENT LEFT WINDOW POINTER
            # q[0] = THE LEFT MOST INDEX, SINCE Q STORES THE INDICES, NOT THE VALUE IN NUMS
            # SO IF THE INDEX AT THE FRONT OF OUR DEQUE IS LESS THAN OUR ACTUAL INDEX, POP IT
            if l > q[0]:
                q.popleft()
            
            # This part is kind of an edge case. Since we initialized l and r to 0, we need to confirm our window is at least size k
            if (r + 1) >= k:
                # At each iteration, we need to add the max value to our output. Since we have a monitonic deque, it'll be the value at the front of our queue
                output.append(nums[q[0]])
                l += 1 # Once we have a window at least size k, make sure it stays size k by incrementing l each time too.
            
            # move the right side of the window too
            r += 1
        
        return output
                