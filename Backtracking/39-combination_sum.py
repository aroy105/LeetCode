class Solution:
    """
    Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. 
    You may return the combinations in any order. The same number may be chosen from candidates an unlimited number of times. 
    Two combinations are unique if the frequency of at least one of the chosen numbers is different.
    The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
    """
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Using a decision tree similar to the one we used in 78. Subsets can yield duplicate solutions, since we can reuse the same numbers
        # We can modify our decision tree, where one branch has all +1 occurences of an element, and the other branch doesn't have any occurences of the element. 
        # I.e. given [x_1, x_2, ...], our first branch is the one that contains 1 or more uses of x_1, and in the second branch, we never see x_1 used again. 
        # Then, one layer down from the first branch, we apply the same decision point. 
        # Thus, the first branch of the first branch will contain all further solutions involving more x_1s, and the second branch won't contain any more x_1s. 
        # Effectively, each layer under the first branch tracks whether corresponding solutions contain +1 x_1 or not, +2 x_1s or not, +3 x_1s or not, and so on. 
        # We will use a pointer called i to denote which elements we can use to form combinations. 
        res = []
        def dfs(i, cur, total): 
            # Solution base case
            if total == target:
                res.append(cur.copy())
                return 
            # Exceeded sum or reached end of candidates list base case
            if i >= len(candidates) or total > target:
                return
            
            # This is the decision point
            # Include candidate, move to next decision point
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            # Don't include candidate, move to next candidate
            cur.pop()
            dfs(i + 1, cur, total) 
        
        dfs(0, [], 0)
        return res