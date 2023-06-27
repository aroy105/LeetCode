class Solution:
    """
    You are given two non-empty linked lists representing two non-negative integers. 
    The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
    """
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # There are two major edge cases to watch. First is two different sized lists, second is when cOut necessitates another digit. 
        
        dummy = ListNode() # This handles many of the edge cases.
        cur = dummy 
        
        
        # While there are still nodes to add or if there is still a carry
        carry = 0
        while l1 or l2 or carry: # The third conditional is already handled, since even if v1 and v2 are zero, carry still gets a node. 
            # If we still have nodes in either linked list, set them to val of node. Else they are 0. 
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            # Compute values for carry and the current node, 
            val = v1 + v2 + carry
            carry = val // 10 
            val = val % 10
            cur.next = ListNode(val)
            
            # Update pointers, 
            cur = cur.next 
            l1 = l1.next if l1 else None 
            l2 = l2.next if l2 else None
        
        return dummy.next
            
            
            