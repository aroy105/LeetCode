class Solution:
    """
    Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
    Each number in candidates may only be used once in the combination.
    Note: The solution set must not contain duplicate combinations.
    """
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Combine the principles from 39. Combination sum and 90. Subsets II. 
        # Essentially, we follow the same recursive and total sum stuff that combination sum had
        # However, we sort and push the pointer like we did in Subsets II 
        
        # Just like in Subsets II, skipping over all instances of x is impossible unless the values are sorted
        candidates.sort()
        res = []
        
        def backtrack(cur, pos, target):
            # Base case for found solution
            if target == 0:
                # Using cur.copy() instead of cur[:] seems to save 0.1 MB for memory. 
                res.append(cur.copy())
                return 
            # Base case for exceeding solution
            if target <= 0:
                return
            
            # Instantiate state variable for previous candidate value, useful for skipping repeated values
            # We instantiate with -1 since all values in the list will be positive.
            prev = -1
            # Go through all the remaining candidates. In first call, this includes all candidates
            for i in range(pos, len(candidates)):
                # If current candidate = prev candidate, go directly to the next for loop iteration 
                if candidates[i] == prev:
                    continue 
                
                # recursively go down first branch, push pointer to next candidate, update how far we are from target
                cur.append(candidates[i])
                backtrack(cur, i + 1, target - candidates[i])
                # Go down second branch in next loop
                # Pop this candidate...
                cur.pop()
                # ...then update prev to candidate. In next loop, we will form a branch that excludes this candidate
                prev = candidates[i]
            
        backtrack([], 0, target)
        return res
            