class Solution:
    """
    Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes),
    write a function to find the number of connected components in an undirected graph.
    """
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # We're going to use the Union Find Algorithm again, just like we did in 684
        dsu = UnionFind()
        # Go through each edge, and add it to our dictionary which stores all the components
        for a, b in edges:
            dsu.union(a, b)
        # For each node, find the parent, and store it in a list. Turn this list into a set, which creates a unique instances of root parents. The length of this is the # of connected components
        return len(set(dsu.findParent(x) for x in range(n)))

# Write a separate class to build out our components
class UnionFind:
    
    def __init__(self):
        self.f = {}
        
    # Recursive solution to find parent
    def findParent(self, node):
        # set the parent to the value for key = node. If no entry exists in our dict, set the parent as the node itself
        parent = self.f.get(node, node)
        # If the node != parent...
        if node != parent:
            # Recursively find the parent of the node, and set it as the value for key = node and the parent itself.
            parent = self.f[node] = self.findParent(parent)
        # Return this top-level parent
        return parent
    
    def union(self, node1, node2):
        # Let's parse this. self.findParent(node2) finds the parent of node2
        # self.findParent(node1) finds the parent of node1
        # Thus, this sets the grandparent of node1 to the parent of node2. This creates a common ancestor for the two nodes (i.e. they're connected)
        self.f[self.findParent(node1)] = self.findParent(node2)