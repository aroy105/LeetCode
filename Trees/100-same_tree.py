class Solution:
    """
    Given the roots of two binary trees p and q, write a function to check if they are the same or not.
    Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
    """
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both trees are empty return true
        if not p and not q:
            return True
        # If p and q are both non-null, and they share the same value, recursively check the same conditions on left and right children
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        # If the above condition failed, return False
        else:
            return False