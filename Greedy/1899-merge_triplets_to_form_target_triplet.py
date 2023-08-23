class Solution:
    """
    A triplet is an array of three integers. You are given a 2D integer array triplets, where triplets[i] = [ai, bi, ci] describes the ith triplet. 
    You are also given an integer array target = [x, y, z] that describes the triplet you want to obtain.
    To obtain target, you may apply the following operation on triplets any number of times (possibly zero):
    Choose two indices (0-indexed) i and j (i != j) and update triplets[j] to become [max(ai, aj), max(bi, bj), max(ci, cj)].
    For example, if triplets[i] = [2, 5, 3] and triplets[j] = [1, 7, 5], triplets[j] will be updated to [max(2, 1), max(5, 7), max(3, 5)] = [2, 7, 5].
    Return true if it is possible to obtain the target triplet [x, y, z] as an element of triplets, or false otherwise.
    """
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()
        # For each triplet
        for t in triplets:
            # If any triplet has a value that is greater than the corresponding target value we need, it is useless, so just skip it.
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            # Go through each value in the triplet
            for i, v in enumerate(t):
                # If the value is equal to the target value, add it to the set. Remember, sets won't store duplicates
                if v == target[i]:
                    good.add(i)
        # good will never exceed the size of 3, but it may undercount if only some of the target elements are reached
        return len(good) == 3