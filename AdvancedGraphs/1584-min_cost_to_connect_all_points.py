import heapq
class Solution:
    """
    You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].
    The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.
    Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.
    """
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # This solution works, but speed and memory is dogshit
        # Minimum Spanning Tree Problem - Can be solved via Prim's or Kruskal's Algo, and we'll use Prim's algo
        # First, we must get the edges i.e. the Manhattan Distances between all the points
        # Then we can just run Prim's Algo, since we're literally creating a minimum spanning tree
        # To create a tree w/o a cycle i.e. extra edges, we only need n - 1 edges, where n is the number of vertices. 
        
        # First, grab the # of vertices, and create an adjacency list 
        N = len(points)
        # The dict willl be organized as i: list of [cost, node]
        adj = {i: [] for i in range(N)}
        # For each point, calculate the Manhattan dist to all other points, and fill in the respective entries in the adj list
        for i in range(N):
            x1, y1 = points[i]
            # Then go through all the other points
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        
        # Now, we run Prim's Algorithm
        res = 0
        # This will be the frontier data structure
        visit = set()
        # This will be our minheap, where we store the [cost, point]
        minH = [[0, 0]]
        # While we haven't visited every node...
        while len(visit) < N:
            # Get the least expensive edge from the minHeap
            cost, i = heapq.heappop(minH)
            # If we have already visited this point, jump to the next iteration
            for i in visit:
                continue
            # Add this point to our MST, and thus, increment our total cost
            res += cost
            # Note that we visited this point
            visit.add(i)
            # For all the neighbors of this vertex, if we haven't visited the neighbors, push onto the heap
            for neighborCost, neighbor in adj[i]:
                if neighbor not in visit:
                    heapq.heappush(minH, [neighborCost, neighbor])
        return res
        