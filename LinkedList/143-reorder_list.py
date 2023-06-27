class Solution:
    """
    Given the head of a singly linked list, reorder the list in the form: 
    L_0 -> L_n -> L_1 -> L_n-1 -> L_2 -> L_n-2 -> ...
    
    Do not return anything, modify head in-place instead.
    """
    def reorderList(self, head: Optional[ListNode]) -> None:
        # If we wanted to find an easy solution, just store all the nodes in an array, and have two pointers at the front and back
        # You can then reorder the list by piecewise moving the front pointer forward and the back pointer backwards. 
        # However we can do this with O(1) memory instead
        # At a high level, use fast and slow pointers to find the middle of the list, and set slow.next to start the second half of the list
        # If the second half of the linked list is reversed, we can use pointers to connect and link the first half to the second half to form the reordered list. 
        
        # First, find the middle of the list, using the Floyd's Tortoise and Hare
        slow, fast = head, head.next 
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next
        
        # Reverse the second half of the list to make it easier to form the answer list
        second = slow.next # This is now the start of the second half of the linked list 
        # This next variable will be used to represent the previous node, as we reverse this mini-linked list.
        prev = slow.next = None # This initializes it to the same node as second (the beginning of second half), while setting it's next node to null
        # As we progress through the second half of the linked list...
        while second:
            tmp = second.next  # Store the next node in memory
            second.next = prev # Set our current node to the node behind it. 
            prev = second # Push the previous node up to our current node for the next part of the iteration
            second = tmp # Set our current node to the next one. 
        
        # After this while loop, the linked list is now segemented into two linked lists, pointing in opposite directions
        # prev will be at the beginning of the second linked list (end of original linked list)
        # Now, merge the first half and the reversed second half. 
        first, second = head, prev 
        # Since the second half of the list could be shorter than the first half (as we used slow.next above to handle both even and odd sized lists), continue until there are no more elements...
        while second:
            tmp1, tmp2 = first.next, second.next # Store the next nodes of first and second in memory.
            first.next = second # The front of the first list points to the front of the second list
            second.next = tmp1 # The front of the second list points to the next value in the first list
            first, second = tmp1, tmp2 # The front of the first and second list is shifted forward one node. 