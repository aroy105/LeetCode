class Solution:
    """
    There are n cities connected by some number of flights. 
    You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.
    You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.
    """
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # We're going to use the Bellman Ford Algorithm to solve this problem (O(E*K)), around BFS. Bellman-Ford is generally (O(E*V)), but we are limited by K v's here. 
        # We can also use this algo for negative weights
        # Since we're allowed k stops, that means we have k + 1 edges we can traverse (cities we stop in don't include origin and destination city)
        
        # We want to track out minimum costs to reach each city, so create a lists which will keep it
        prices = [float("inf")] * n
        # Naturally, the cost to reach the origin city is zero
        prices[src] = 0

        # Now, we iterate k + 1 times, to represent the max k + 1 edges we can traverse
        # This is kind of like BFS, since we only explore all the neighboring edges at each iteration. 
        for i in range(k + 1):
            # We'll now create a copy of prices, which will replace it once we've checked all edges in this iteration. 
            # We created a copy to preserve the previous costs as we check every edge. 
            # There's a step where we check if the price to reach a source node is infinity, and if it is, we skip it
            # If we edit our prices list as we iterate through all the edges, we'll end up going through every node in the first iteration, 
            # as the destination nodes will become our next source nodes. We don't want to visit these new frontier until the next iteration, 
            # or we may never visit these at all if it takes place in iteration k+1. Thus, we need a copy.
            tmpPrices = prices.copy()
            # We'll go through every flight in our array, although due to the conditions, it's more like a BFS, where we expand neighboring nodes
            for s, d, p in flights:  # s=source, d=dest, p=price
                # If we can't reach the origin of this flight as of yet i.e. price == infinity, skip this flight and check the next flight
                if prices[s] == float("inf"): 
                    continue
                # If price to get to the origin + the price to get to the destination < previously recorded cost to get to the destination, update price
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
            # Set our old prices to the new prices discovered in this iteration
            prices = tmpPrices
        # If we weren't able to reach our destination i.e. cost == inf, return -1. Else, return the recorded cost to reach the destination
        return -1 if prices[dst] == float("inf") else prices[dst]