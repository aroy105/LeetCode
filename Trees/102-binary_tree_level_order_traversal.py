import collections
class Solution:
    """Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level)."""
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Our list will store the values of the nodes in a level-order
        res = []
        # We will use a deque to start at the top level.
        q = collections.deque()
        # Initialize the while loop to go through all the trees
        if root:
            q.append(root)
        # While there are still nodes in the tree
        while q:
            # We will store a mini-list
            val = []
            # From left to right, 
            for i in range(len(q)):
                # The left most node in q, which is the left-most, highest, unexpanded node will be stored 
                node = q.popleft()
                # Since it is now expanded, place it in the res list.
                val.append(node.val)
                # Add the children of the expanded node to the end of the list. 
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                # At this point, the current node has been expanded. 
                # In the next iteration, we move to either 1) the node directly to the right of the just expanded node, 
                # or 2) the node we just expanded was the last in it's level. 
                # However, nodes from the children of prior nodes may still exist, and these children nodes were placed at the end of the list in level order.
                # Thus we start it again

            # At this point all nodes have been expanded. 
            res.append(val)
        return res
        