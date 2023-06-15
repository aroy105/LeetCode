class Solution:
    """
    Given head, the head of a linked list, determine if the linked list has a cycle in it.

    There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. 
    Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
    """
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # If we maintain a hashmap where the keys are the nodes, and we ever get a hit on our hashmap as we traverse through the list, then it has a cycle
        # However, we can also do it with two pointers, this is called Floyd's Tortoise and Hare
        # Basically, there's a slow pointer that moves one node at a time, and a fast pointer that moves two nodes at a time. 
        # If the fast pointer reaches a null node, then there should be no cycles, as it terminated. 
        # If the slow pointer is ever at the same spot as a fast pointer after the race has started, then there must habe been a cycle
        # This is because the fast pointer caught up to the slow pointer after crossing more distance in a cycle
        slow, fast = head, head
        
        # While fast and the next node is not null (since it skips by two)
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
            if slow == fast:
                return True
        return False