class Solution:
    """
    A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. 
    A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
    The path sum of a path is the sum of the node's values in the path.
    Given the root of a binary tree, return the maximum path sum of any non-empty path.
    """
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # here's an observation. You can end up in a situation where your max possible path can entirely be contained in a subtree, rather than a long chain
        # When we analyze what the max sum of a path would be entirely through a lower subtree, this is called splitting. 
        res = [root.val]
        
        # This will return the max path sum without "splitting" i.e. the chain
        def dfs(root):
            # reached null child i.e. end of bst
            if not root:
                return 0 
            
            # Recursively check the left and right paths
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            # This handles negative paths, and it basically ensures we don't go down these routes. 
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)
            
            # Check a subtree split, and see if we get a higher value
            res[0] = max(res[0], root.val + leftMax + rightMax)
            
            # Return the maximum path subsum up the recursive stack
            return root.val + max(leftMax, rightMax)
        
        dfs(root)
        return res[0]