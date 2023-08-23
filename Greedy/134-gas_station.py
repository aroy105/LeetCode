class Solution:
    """
    There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].
    You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. 
    You begin the journey with an empty tank at one of the gas stations. Given two integer arrays gas and cost, return the starting gas station's index if
    you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique
    """
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # We kind of assume that the sum of the gas is greater than the sum of the costs 
        # Previous iterations of the problem did a if sum(gas) < sum(cost): return -1, but speed + memory dropped by 20%. 
        total_gas, remaining_gas, start_index = 0, 0, 0
        # Go through every gas station
        for i in range(len(gas)):
            # Update our total and remaining gas
            total_gas += gas[i] - cost[i]
            remaining_gas += gas[i] - cost[i]
            # This part took me a second to understand, since I thought if we failed at the given start index, we'd need to recheck the previous values that wrap around
            # No matter where you start, the lowest gas tank always happens at same index. Thus, always pick i + 1 as the starting point, because it'll only go up from there
            if remaining_gas < 0:
                # Reset, and start at next index
                remaining_gas = 0
                start_index = i + 1 
                # No further steps are needed, since all previous values were chained together up to i . If sum(gas) >= sum(cost), then going from 
                # i - 1 to i + 1 can be done 
                
        # If we still had gas/just finished by the time we reached the end, return the start index
        if total_gas >= 0:
            return start_index
        else:
            return -1