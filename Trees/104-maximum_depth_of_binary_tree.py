from collections import deque
class Solution:
    """Given the root of a binary tree, return its maximum depth."""
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """Recursive DFS"""
        # Base Case
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
    def maxDepth(self, root):
        """Iterative DFS"""
        # Build a stack that will contain unexamined nodes
        stack = [[root, 1]]
        res = 0 
        
        # While all the nodes are yet to be examined....
        while stack:
            # Remove the latest element from the stack
            node, depth = stack.pop()
            # If the element we popped was a node, add it's children
            if node:
                # At this point, we have found a potential new max-depth, so update accordingly
                res = max(res, depth)
                # Record an updated depth for the children
                stack.append([node.left, depth+1])
                stack.append([node.right, depth+1])
        return res
    
    def maxDepth(self, root):
        """BFS"""
        q = deque()
        # If we have a node right now, add it to the end of the deque
        if root:
            q.append(root)
        
        level = 0 
        
        # While there are nodes in the deque
        while q:
            # This is interesting, basically as we remove the parent nodes from the front of the list, we add the children to the end of the list
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            # At this point, all the parent nodes are removed, and their children are there in order, so we now bump the level and repeat
            level += 1 
        # At this point, all nodes exhausted, and we have found the deepest node. 
        return level
        
                