import collections, heapq
class Solution:
    """
    You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui
    is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.
    We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. 
    If it is impossible for all the n nodes to receive the signal, return -1.
    """
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # This problem will require Dijkstra's Algo
        # Create a dictionary of all the nodes, where u is the source node, v is the target, and w is the time taken
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))
        # Create a minHeap to store min edges, and create a visited set
        minHeap = [(0, k)]
        visit = set()
        # Initialize the time
        t = 0
        # We will run BFS, so while the heap still has elements 
        while minHeap:
            # Pop the element in the heap which is closest to the source i.e. the one with the lowest time to reach
            w1, n1, = heapq.heappop(minHeap)
            # If we have already visited this node previously, a quicker path already exists, so go to the next iteration
            if n1 in visit:
                continue
            # Add this node to the visited set
            visit.add(n1)
            # Set t to the time it took to reach this node
            t = w1
            # For every neighbor of this node
            for n2, w2 in edges[n1]:
                # If we haven't already visited the neighbor
                if n2 not in visit:
                    # Add this node to the heap, and set the time it takes to reach this node as (time it takes to reach n1) + (time to reach n2 from n1)
                    heapq.heappush(minHeap, (w1 + w2, n2))
        # Return t if we were able to visit every node and check it via djikstras. If we couldn't reach every node, return -1
        return t if len(visit) == n else -1
        