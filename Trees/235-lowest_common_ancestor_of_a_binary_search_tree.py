class Solution:
    """
    Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
    According to the definition of LCA on Wikipedia: 
    “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
    """
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # The lowest common ancestory occurs when there is a split between p and q i.e. you need to search down different subtrees. 
        # The second you're not searching in the same subtree, you've found the lowest point before they diverge. 
        # One edge case is if p or q is the node we're checking, then that is the LCA
        cur = root 
        while cur: 
            # Check if both values will go to the right subtree
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            # Check if both values will go to the left subtree
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            # At this point, there is either a divergence or cur = p or cur = q
            else:
                return cur