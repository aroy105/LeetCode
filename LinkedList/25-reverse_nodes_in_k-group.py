class Solution:
    """
    Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
    k is a positive integer and is less than or equal to the length of the linked list. 
    If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
    You may not alter the values in the list's nodes, only nodes themselves may be changed.
    """
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # We use a dummy node, because the head may be modified during the reversal
        # This helps with a lot of edge cases. 
        dummy = ListNode(0, head)
        groupPrev = dummy 
        
        while True:
            # This is the last node in each group
            kth = self.getKth(groupPrev, k)
            # If we have a group with < k elements i.e. k is Null
            if not kth:
                break
            # Variable to store the first value not in the k-group
            groupNext = kth.next
            
            # Now the following while loop will reverse the group
            # Previous node is set to next group's beginning value (since we are reversing), and curr is set to beginning of k-group
            prev, curr = kth.next, groupPrev.next
            while curr != groupNext: # Until we reach the end of our group....
                # As we reverse the nodes, store curr.next in memory as temp
                tmp = curr.next 
                # point curr.next to the "previous node", on first iteration it is the 1st val in next group
                curr.next = prev 
                # Set our new "previous ptr" to our current node
                prev = curr 
                # Set curr ptr to the next value in the group to be reversed
                curr = tmp
            
            # Store the former first node in the group. It is now the last node in the group due to reversal in while loop
            tmp = groupPrev.next
            # set the previous group's next ptr to the last node in the group (which has become the first node after the inner while loop)
            groupPrev.next = kth
            # Update the previous group's pointer to be the last value of our current group, and begin the cycle anew. 
            groupPrev = tmp
        return dummy.next
            
    def getKth(self, curr, k):
        """Helper function to get to the kth node"""
        while curr and k > 0:
            curr = curr.next 
            k -= 1
        return curr
        