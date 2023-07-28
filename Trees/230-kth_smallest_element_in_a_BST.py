class Solution:
    """Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree."""
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Basically visit every element in-order, and we will use an iterative solution
        stack = []
        curr = root # Pointer for where we are currently at
        
        # While the stack and our pointer are not null...
        while stack or curr: 
            # While the pointer isn't null
            while curr:
                # Add all the elements of the left most path
                stack.append(curr)
                curr = curr.left
            # At this point, we exceeded how far left we could go and ended up at a null child.
            # So we back up, and set curr to the smallest value we have
            curr = stack.pop()
            k -= 1 # In each loop, we remove all the values smaller than the kth smallest element
            # If we've gone through k while loops (i.e. k = 0), this is the kth smallest element
            if k == 0:
                return curr.val 
            # We exhaused all options all the way down the the left, but lower values still may exist in right branches farthest down the chain, so restart the process and check those too. 
            curr = curr.right 
            