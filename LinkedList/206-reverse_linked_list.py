class Solution:
    """Given the head of a singly linked list, reverse the list, and return the reversed list."""
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Two solutions exist, iterative and recursive
        self.iterative(head)
    
    def iterative(self, head):
        # O(n) time, O(1) memory
        prev, curr = None, head
        
        while curr: # While the current pointer is not equal to null 
            # Make a new variable and set it to the next pointer
            next = curr.next 
            # Have our current pointer point behind
            curr.next = prev 
            # Set our previous pointer to the current one
            prev = curr 
            # Set our current pointer to the next one
            curr = next 
        return prev
    
    def recursive(self, head):
        # O(n) time and memory
        
        # Base case, if head is null, return null
        if not head:
            return None
        
        newHead = head
        # if the next node is not null
        if head.next:
            # make a recursive call to the next node, and set it to the newHead value
            newHead = self.recursive(head.next)
            # Set the "next" attribute of the next node to our current node 
            head.next.next = head 
        
        # Unlink the current node's next pointer
        head.next = None 
        
        return newHead