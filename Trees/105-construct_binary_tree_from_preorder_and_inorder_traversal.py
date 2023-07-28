class Solution:
    """Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree."""
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # We know two facts
        # 1) The first value in a preorder traversal is the root
        # 2) In inorder traversal, once you find the root via fact 1, values to the left of the root are in the left subtree, and values the right of are in the right subtree
        # Using this segmentation, we can recursively find the roots of the tree, then each of it's subtrees, and break apart the left and right halfs. 
        
        # Base case
        if not preorder or not inorder:
            return None 
        
        root = TreeNode(preorder[0]) # Set the root of our tree to first value of preorder (Fact # 1)
        mid = inorder.index(preorder[0]) # Grab the index of the root in preorder
        # Recursively go down the left and right subtrees, by setting the left and right node to be recursive calls
        # For the left, the first value is our old root. Collect all the values in the left subtree 
        # That means all inorder values up to but not including the midpoint are valid (Fact # 2)
        # The number of left subtree values are obviously the same in both pre and inorder traversal. Only difference is where they appear in the list. 
        # This block of left subtree values appears after the root in preorder traversal. mid also represents the # of values in the left subtree, so their length is [1:mid+1]
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[ : mid])
        # similar process is used on the right.
        root.right = self.buildTree(preorder[mid + 1 : ], inorder[mid + 1 : ])
        return root