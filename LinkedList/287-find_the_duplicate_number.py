class Solution:
    """
    Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
    There is only one repeated number in nums, return this repeated number.
    You must solve the problem without modifying the array nums and uses only constant extra space.
    """
    def findDuplicate(self, nums: List[int]) -> int:
        # This is a linked list cycle problem, and we then need to use Floyd's Algorithm
        
        # Not really intuitive, but if there are n + 1 integers and only one integer is repeated twice, we can actually turn this into a Linked List problem.
        # How? Imagine each value represents a further index to point to in the list. The duplicates create a cycle, as depicted below
        
        # Idx: 0 1 2 3 4 
        # Val: 1 3 4 2 2
        # Creates...           1 -> 3 -> 2 <-> 4
        
        # As from previous problems, you create a slow and fast pointer, and see where they intersect. This is the first phase of the algo. Leave the slow pointer there
        # Create a second slow pointer, and iterate until both slow pointers intersect. Their new intersection will always be the result
        
        # This works because dist between the 1st intersection and the beginning of cycle (2nd intersection point) will always be same as dist between head & beginning of cycle.
        # This is true if we graph it out a little. Given....
        # Head -> P nodes -> start of cycle -> first intersection -> end/beginning of cycle. 
        # Let the dist from start of graph to start of cycle be P. Let length of cycle be C. Let x be distance between first intersection and beginning of cycle. 
        # Then, C - x is distance from start of cycle to first intersection point. If we do a little algebra, we can start from the fact that 2*slow = Fast (this is for distance travelled)
        # Fast = P [distance to get to cycle] + (C - X) [first time it hits future intersection point] + C [when it actually intersects with slow pointer one cycle later]
        # Fast = P + 2C - X 
        # Likewise, in our first iteration, the slow pointer travelled P [dist to cycle] + (C - X) [where it intersects with fast pointer]. 
        # Thus, 2*slow = fast -> 2*(P + C - X) = P + 2C - X, which simplifies to P = X. 
        # Technically, math gets a little funky if P is super long, since multiple traverals of cycle may be needed. In that case, fast = P + N*C - X
        
        # We know zero is never a part of our cycle, since problem states all in range of [1, n]
        slow, fast = 0, 0 
        while True: 
            # Equivalent of slow = slow.next and fast = fast.next.next
            slow = nums[slow]
            fast = nums[nums[fast]]
            # first intersection found
            if slow == fast:
                break # Essentially do while loop
            
            slow2 = 0 
            while True:
                slow = nums[slow]
                slow2 = nums[slow2]
                if slow == slow2:
                    return slow 
            
        