class Solution:
    """
    You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.
    You can either start from the step with index 0, or the step with index 1. 
    Return the minimum cost to reach the top of the floor.
    """
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Go backwards, starting from the second to last step to the beginning, and store in each step the cheapest way to the top from that point
        # From the nth step, we can then just do a 1 jump. From the n-1th step, we can do a two jump. 
        # We need to start calculating our costs from the n-2th step, since this is the last place where it's impossible to reach the top for free
        # We then work backwards, and for each step, add the step cost which it's cheapest to jump to and incur
        # This is a greedy approach
        for i in range(len(cost) - 3, -1, -1):
            # In the first iteration, add whichever step cost it's cheapest to jump to and incur, either the n-1 step (1 jump) or n step (2-jump)
            # iteratively add the accumulated costs down the chain
            cost[i] += min(cost[i + 1], cost[i + 2])
        
        # At this point, every step has the cost of cheapest path from that point. Therefore, steps 1 and 2 have the accumulated costs for going all the way up
        # Pick which path is cheaper from the two
        return min(cost[0], cost[1])