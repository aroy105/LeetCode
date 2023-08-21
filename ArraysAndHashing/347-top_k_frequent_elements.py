class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order."""

        # The naive approach is go through list with hashmap where we have number: frequency. Then use a max heap to get the k elements

        # However, we know that the max frequency of an element has to be the length of the list (n)
        # So what if we had a list-backed hashmap in the form frequency: number? The number of keys would max out at n given this observation
        # This is a kind of bucket sort
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        # First, count the number of times each element appears
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        # Then, for each number: frequency pair, index by frequency and add the corresponding number
        for n, c in count.items():
            freq[c].append(n)
        
        # At this point, we have a hashmap, where all numbers are sorted into respective frequency values
        
        # Now, essentially iterate from highest to lowest values. When we get to the kth element, return. 
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
            if len(res) == k:
                return res