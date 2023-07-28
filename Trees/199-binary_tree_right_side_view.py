from collections import deque
class Solution:
    """Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom."""
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # We can use BFS (aka level order traversal)
        # For each level of the tree we basically want the right most value
        # We will use a queue which will store all the current values in a level. 
        # We store the right most value of each level, and then expand to the children of the current level in the queue. 
        res = []
        q = deque([root])
        # While there are non-null children
        while q: 
            rightSide = None
            # The current number of parents in q
            qLen = len(q)
            # Go through ONLY the parents
            for i in range(qLen):
                # Store the parent who's children we will add to queue
                node = q.popleft()
                # If the parent wasn't null... , and add it's children. When the for loop terminates, rightSide will be set to the rightmost parent
                if node:
                    # set rightSide to the just expanded parent
                    rightSide = node 
                    # Add the children, to be evaluated in the next while loop.
                    q.append(node.left)
                    q.append(node.right)
            # By the time this for loop ends, rightSide will be set to the farthest right non-null parent
            if rightSide:
                res.append(rightSide.val)
        return res