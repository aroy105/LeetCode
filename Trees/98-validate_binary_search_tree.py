class Solution:
    """Given the root of a binary tree, determine if it is a valid binary search tree (BST)."""
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Create a helper function
        def valid(node, left, right):
            # If we reached a null node, we reached the end i.e. everything before has been valid
            if not node:
                return True 
            # If the node in question can't abide by the left or right restrctions on it as a BST, it is clearly not valid
            if not (left < node.val < right):
                return False 
            # Recursively go down the left and right subtree, and ensure they're both valid 
            # For the left child, it and all it's descendents must be smaller than the root it descended from, so we decrease the upper bound
            # For the right child, it and all it's descendents must be greater than the root it descended from, so we increase the lower bound
            return valid(node.left, left, node.val) and valid(node.right, node.val, right)
        # Start at the root and set the bounds to unbounded values. 
        return valid(root, float("-inf"), float("inf"))