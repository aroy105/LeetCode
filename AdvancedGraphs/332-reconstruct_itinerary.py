import collections
class Solution:
    """
    You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. 
    Reconstruct the itinerary in order and return it. All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". 
    If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.  
    For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
    You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.
    """
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Create the adjacency list (or rather, deque), for each ticket
        adj = {u: collections.deque() for u, v in tickets}
        # We always start from JFK, so add it as our initial value
        res = ["JFK"]
        # Now, arrange all our tickets in lexical order, and then it'll be placed into the adjacency list in correct order
        tickets.sort()
        # Place each ticket into the adjacency list
        for u, v in tickets:
            adj[u].append(v)
        
        # Use DFS to go through array
        def dfs(cur):
            # Base Case if we traversed every edge (nodes in result = # of tickets + 1 i.e. nodes = edges + 1)
            if len(res) == len(tickets) + 1:
                return True
            # Base case if the current airport we're at has no outgoing flights i.e. we're stuck and can't continue our travels
            if cur not in adj:
                return False
            # Create a temporary list of places we can visit from the airport, so we can iterate through it without being stuck in an infinitely cycling through it
            # We'll need to pop from the left for one dfs path, but we'll need to add it back. We'll need a copy of the list so we don't iterate down the added back path
            # The removal down one DFS path represents using that ticket
            temp = list(adj[cur])
            # For each outgoing flight from our airport...
            for v in temp:
                # Pop the current flight from our list of outgoing flights, and add it to results
                adj[cur].popleft()
                res.append(v)
                # If a path that ultimately hits every edge can be generated going down this path, return the generated path
                if dfs(v):
                    return res
                # Backtrack, and go down the next path. Remember to add back this flight to the adjacency list, so that it can be counted for future trackings
                res.pop()
                adj[cur].append(v)
            # If we have gone through every flight from this node and found nothing, it's cursed, and we can't achieve anything from this airport. Return False
            return False

        # Run dfs from the origin and return the resulting array.
        dfs("JFK")
        return res
        