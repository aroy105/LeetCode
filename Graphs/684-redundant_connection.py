class Solution:
    """
    In this problem, a tree is an undirected graph that is connected and has no cycles.
    You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added.
    The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. 
    The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.
    Return an edge that can be removed so that the resulting graph is a tree of n nodes. 
    If there are multiple answers, return the answer that occurs last in the input.
    """ 
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # While a naive O(n^2) solution can be used, an O(n) solution exists if we use a Union Find Algorithm
        # There is a key observation, where we need to realize that with n nodes and n-edges, we always have a cycle. 
        # Consider 4 nodes and 4 edges, and how only with three edges can we have a tree. 
        # Once we noticed there's an edge that created another path from point a to b, we return it
        # We will use Union find by rank, where a node with the most connections is the root of the tree
        
        # Store parent and rank of each node
        parent = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)
        
        # This function will take in a node, and it will go all the way up the chain to find the root node
        def find(n):
            # Given n, find it's immediate parent node
            p = parent(n)
            # While the immediate parent node is not equal to the parent of the immediate parent node
            while p != parent[p]:
                # Set the value of the immediate parent node to the immediate parent's parent node
                parent[p] = parent[parent[p]]
                # Set the immediate parent node to it's parent, thus moving up the chain
                p = parent[p]
            # At this stage, the parent node is set to the top most parent of the node we initially inputted. 
            return p
        
        # return false if a union was already made prior, and an excess edge is about to be added. 
        def union(n1, n2):
            # Find the parents 
            p1, p2 = find(n1), find(n2)
            # If the two nodes share the same parent, an excess edge is about to be added, and we need to return false
            if p1 == p2:
                return False
            # If p1 is of a higher rank, set it as the parent of p2, and update the rank of p1
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return True
        
        # Go through all the edges
        for n1, n2 in edges:
            # If the excess edge was found, return the edge
            if not union(n1, n2):
                return [n1, n2]