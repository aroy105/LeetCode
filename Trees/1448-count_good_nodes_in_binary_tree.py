class Solution:
    """
    Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.
    Return the number of good nodes in the binary tree.
    """
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, maxVal):
            # Terminating base case
            if not node:
                return 0
            # We have found a good node if the value in the node is greater than the maxVal in the chain
            # Set res to 1 if it's good, otherwise set it to zero
            res = 1 if node.val >= maxVal else 0 
            # Reevaluate the largest maxnode
            maxVal = max(maxVal, node.val)
            # Recursively add up all the res down the left and then down the right
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            return res 
        # Initialize with the root and its value, since this will be the first value which all other values in the route will be comapred against. 
        return dfs(root, root.val)