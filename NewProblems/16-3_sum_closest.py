class Solution:
  """
  Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

  Return the sum of the three integers.

  You may assume that each input would have exactly one solution.
  """
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # This solution only works if nums is sorted, as we'll break it into a Two Pointer Sub Problem
        nums.sort()
        # We will need to record both our best answer so far, along with what makes it the best answer i.e. the difference between the answer and the target
        difference = float("inf")
        answer = 0
        # We'll set i to go through the list, while j and k are initially set right after i and at the end of the list
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            # Now, we do Two Pointer
            while j < k:
                # At the moment, calculate the sum 
                current_sum = nums[i] + nums[j] + nums[k]
                # If the sum is the target, just return the target
                if current_sum == target:
                    return target
                # If our sum is better than the previous answer, update the answer and it's difference
                if abs(target - current_sum) < difference:
                    difference = abs(target - current_sum)
                    answer = current_sum
                # If our answer is less than the target, increase our sum by moving j up. If the answer is greater than the target, decrease the sum by moving k down
                if current_sum < target:
                    j += 1
                else:
                    k -= 1
        
        return answer
