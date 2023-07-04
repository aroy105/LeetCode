class Solution:
    """Given the root of a binary tree, invert the tree, and return its root."""
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base Case
        if not root:
            return None

        # Switch left and right for this node
        tmp = root.left
        root.left = root.right 
        root.right = tmp
        # recursively affect children
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root