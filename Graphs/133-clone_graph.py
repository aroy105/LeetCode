"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    """
    Given a reference of a node in a connected undirected graph.
    Return a deep copy (clone) of the graph.
    Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.
    """
    def cloneGraph(self, node: 'Node') -> 'Node':
        # Create a global dictionary 
        # oldNode: copy of node we made
        oldToNew = {}
        # Use a dfs to go through each node
        def dfs(node):
            # If the node we're looking at now is already in the dictionary, just return the copy to be added to our new copies neighbor
            if node in oldToNew:
                return oldToNew[node]
            # Create a copy if the node wasn't in the dictionary
            copy = Node(node.val)
            # Add this node in the original value as the key, with copy we made as the value
            oldToNew[node] = copy
            # For each of the neighbors, go through and run dfs through them
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            # Return the original node
            return copy
        
        # Handles base case and starts with base case in one liner
        return dfs(node) if node else None