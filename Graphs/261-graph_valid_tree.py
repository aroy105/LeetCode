class Solution: 
    """
    You have a graph of n nodes labeled from 0 to n - 1. 
    You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.
    Return true if the edges of the given graph make up a valid tree, and false otherwise.
    """
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Given a empty graph, return true, since this is technically a valid tree
        if not n:
            return True
        # Create the adjacency list
        adj = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        visit = set()
        # Run DFS, we use prev to make sure we don't generate a false positive cycle. The node we just came from will be our parent node, and we don't want to count going backwards as a DFS route. 
        def dfs(i, prev):
            # If we have already visited the node, a cycle has been generated
            if i in visit:
                return False

            # Add the node ot our visited set, and go through each edge in the adjacency list
            visit.add(i)
            for j in adj[i]:
                # If the edge is the one we just came from, don't run DFS down it
                if j == prev:
                    continue
                # If a cycle is found at any point recursively down the edges, return False
                if not dfs(j, i):
                    return False
            # No cycles were found, so return True
            return True
        # Using -1 as prev (since we don't need to worry about accidentally backtracking at the root), run dfs from the root....
        # We also need to see if the # of nodes == len(visit). If not, we didn't visit every node i.e. there are nodes which existed that weren't in our tree, so the whole thing is not in a tree
        return dfs(0, -1) and n == len(visit)