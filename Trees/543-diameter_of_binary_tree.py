class Solution:
    """
    Given the root of a binary tree, return the length of the diameter of the tree.
    The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
    The length of a path between two nodes is represented by the number of edges between them.
    """
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
    
        def dfs(root):
            # This keyword in python lets us use variables that are traditionally outside of their regular scope. 
            # Could just make a helper function that takes res as an input, not sure which is better. 
            nonlocal res
            # For empty nodes, return 0, since we can't traverse here
            if not root:
                return 0
            # Do DFS on the left and right
            # This yields the max heights on the left and the right
            left = dfs(root.left)
            right = dfs(root.right)
            # Update our result if a higher diameter is found
            res = max(res, left + right)
            # We need to add one depending on the node so that the node can be connected to the larger left or right chain.
            return 1 + max(left, right)
        
        # Actually run the function and return the result
        dfs(root)
        return res
    
    
            