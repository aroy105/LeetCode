class Solution:
    """
    Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
    Return the head of the merged linked list.
    """
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode() # Set to null, so we can always keep track of the head of the list
        tail = dummy # We'll track the tail 
        
        # While both lists have elements in them
        while list1 and list2:
            # set the lower of the two top values to the next value in our chain, and then pop it off the list
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next 
            else:
                tail.next = list2 
                list2 = list2.next 
            # Move the tail pointer down one more node (this sets it to the end of chain)
            tail = tail.next
        
        # At this point, at least one, if not both, of the lists are empty
        # These next lines just append the rest of either of the nonempty lists to the end of our current chain.
        if list1:
            tail.next = list1 
        elif list2:
            tail.next = list2 
        
        return dummy.next