import heapq
class Solution:
    """
    You are given an array of integers stones where stones[i] is the weight of the ith stone.
    We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. 
    The result of this smash is:
        If x == y, both stones are destroyed, and
        If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
    At the end of the game, there is at most one stone left.
    Return the weight of the last remaining stone. If there are no stones left, return 0.
    """
    def lastStoneWeight(self, stones: List[int]) -> int:
        # We need to use a heap to store and simulate the heaviest stones that will be collided
        # Since python only supports a MinHeap, we can just multiply all numbers by -1 to have it sort by MaxHeap
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            first = abs(heapq.heappop(stones)) # heaviest
            second = abs(heapq.heappop(stones)) # second heaviest/equal in weight
            # If second stone will be totally obliterated by first
            if second < first: 
                # Return what's left of first back into stones (multiply by -1 since it is a MaxHeap)
                heapq.heappush(stones, -(first - second))
                
        stones.append(0) # A zero weight stone handles an edge case of an empty stones list. This is also the minimum answer for any such list
        return abs(stones[0])