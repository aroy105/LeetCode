class Solution:
    """Given a binary tree, determine if it is height-balanced (depths of two subtrees never differ by more than one)"""
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True, 0]
            
            left, right = dfs(root.left), dfs(root.right)
            # As long as left and right are balanced, and as long as the difference in their heights is lte to 1, the node is still balanced
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1 
            # Return that the node is balanced, and it's height is one level above the higher of the two subtrees
            return [balanced, 1 + max(left[1], right[1])]
        return dfs(root)[0]