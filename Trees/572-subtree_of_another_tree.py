class Solution:
    """
    Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
    A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.
    """
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # If the subroot is null, it is trivially a subtree of the larger tree
        if not subRoot:
            return True
        # At this point we know subroot is non-null. If root however is null, then it is impossible to have subtrees
        if not root:
            return False
        # Check if the tree and subtree are the same
        if self.sameTree(root, subRoot):
            return True
        # Recursively check if the left child or the right child matches the subtree
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def sameTree(self, s, t):
        """Explanation in 100-same_tree problem"""
        if not s and not t:
            return True
        if s and t and s.val == t.val:
            return self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right)
        return False