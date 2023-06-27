class Solution:
    """Given the head of a linked list, remove the nth node from the end of the list and return its head."""
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Like most linked list problems, use Two Pointers. 
        
        # If we make the difference between the left & right pointer n, then by the time that the right pointer reaches the end, the left pointer will be at the desired node.
        # Note this is not a fast or slow pointer thing, they both move one node at a time after the right pointer gets n spaces ahead of the left pointer.
        # Set the left ptr at a dummy node pointing to the first node. When the right pointer reaches the end, the left ptr will be at the node before the one we must remove
        
        # Set left to right before head
        dummy = ListNode(0, head)
        left = dummy 
        # Set right n spots ahead
        right = head
        while n > 0 and right:
            right = right.next 
            n -= 1 
        
        # While the right pointer is still a node (this is how we iterate forward)
        while right:
            left = left.next 
            right = right.next 
        
        # Dereference the node to remove. 
        left.next = left.next.next 
        
        return dummy.next # Remember the dummy node hasn't changed. 
        
        