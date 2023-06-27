class Solution:
    """
    You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
    Merge all the linked-lists into one sorted linked-list and return it.
    """
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Naive approach is O(k*n)
        # Merge sort become O(n*log(k))
        if not lists or len(lists) == 0: return None 
        
        while len(lists) > 1:
            mergedList = []
            # We merge pairs of linked lists, so we increment by 2
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i+1) < len(lists) else None # If the len of lists is odd, this may be out of index
                mergedList.append(self.mergeList(l1, l2))
            lists = mergedList
        return lists[0]
    
    def mergeList(self, l1, l2):
        """This is just our helper function, this is the easy part, basic Merge Sort"""
        dummy = ListNode()
        tail = dummy 
        
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1 
                l1 = l1.next 
            else:
                tail.next = l2 
                l2 = l2.next 
            tail = tail.next 
        if l1:
            tail.next = l1 
        if l2:
            tail.next = l2
        return dummy.next 