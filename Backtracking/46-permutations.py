class Solution:
    """Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order."""
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Like many other similar problems, we will use backtracking and recursion here
        # Essentially, we have len(nums) branches for all the ways to start a permutation
        # Then those branches have len(nums - 1) branches for the remaining characters
        # In code, we simulate this by recursively shearing off the first value
        
        # Since permute() is recursively called, only the top level res is what is returned
        # This is local, which is fine, since we don't need a power set. 
        res = [] 
        # Base case when we go all the way down the decision tree
        if len(nums) == 1:
            return [nums[:]]
        
        # Create branches for all the remaining numbers
        for i in range(len(nums)):
            # Remove the value we just examined
            n = nums.pop(0)
            # Recursively run this function on the rest of the integers, and return the result in perms
            perms = self.permute(nums)
            # To each generated permutation, add the value we removed to make it 
            for perm in perms:
                perm.append(n)
            # Tack on the values in perms to the end of the results tab
            res.extend(perms)
            # Move the value that was popped from the front to the back. 
            # This way, it'll be considered in the later for loop iteration
            nums.append(n)
        return res