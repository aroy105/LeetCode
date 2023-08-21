class Solution:
    """
    There are n cars going to the same destination along a one-lane road. The destination is target miles away.
    You are given two integer array position and speed, both of length n, where position[i] is the position of the ith car and speed[i] is the speed of the ith car (in miles per hour).
    A car can never pass another car ahead of it, but it can catch up to it and drive bumper to bumper at the same speed. The faster car will slow down to match the slower car's speed. 
    The distance between these two cars is ignored (i.e., they are assumed to have the same position).
    A car fleet is some non-empty set of cars driving at the same position and same speed. Note that a single car is also a car fleet.
    If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet. Return the number of car fleets that will arrive at the destination.
    """
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # We can view this as a system of linear systems. 
        # Given the inital position and the speed, we can just see at what time they intersect, and determine the length of a fleet
        # If we calculate when they arrive at the desitination, any two that collide can be collapsed into a single unit
        pair = [[p, s] for p, s in zip(position, speed)]
        stack = []
        for p, s in sorted(pair)[::-1]: # Reverse Sorted Order
            stack.append((target - p)/s)
            # If the car behind reaches the end destination before the car in front of it, they must collide
            if len(stack) >=2 and stack[-1] <= stack[-2]:
                stack.pop() # Add it to the car fleet
        return len(stack)