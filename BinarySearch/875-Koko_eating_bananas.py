import math
class Solution:
    """
    Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
    Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. 
    If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
    Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
    Return the minimum integer k such that she can eat all the bananas within h hours.
    """
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Basically Koko, wants to eat all the bananas, which are separated into n piles, and she will take an hour to finish each pile. 
        # To be able to eat all the piles would take n hours, since she always takes 1 hour per pile. 
        # We then know that logically, h (how long the guards are out) >= n, since the problem constrains requires that she eats all bananas from n piles
        # Always good to talk to the interviewer to double check this and explain the logic! 
        # 
        # A Brute force approach would be to go through all values from k to max(p) [i.e. the fastest speed that ensures the largest pile is eaten in 1 hour].
        # For all the k-values between 1 and max(p), we'd need to find the minimum k where the time it takes to eat the bananas <= h
        # We can use Binary Search to speed this process up
        
        l, r = 1, max(piles) 
        res = max(piles) # This is the worst-case solution under question parameters
        
        # until l and r converge on an answer
        while l <= r:
            k = (l + r) // 2
            
            totalTime = 0
            # Calculate totalTime to each all bananas in all piles
            for p in piles:
                totalTime += math.ceil(p / k)
            # Determine if the time to eat the banans is less than the time for the guards to come back
            if totalTime <= h:
                # A new minimum k is found, so ignore all higher rates
                res = min(res, k)
                r = k - 1
            else:
                # This time doesn't work, so ignore all lower rates
                l = k + 1
        
        return res
        
        