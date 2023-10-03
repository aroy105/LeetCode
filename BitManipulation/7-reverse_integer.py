import math
class Solution:
    """
    Given a signed 32-bit integer x, return x with its digits reversed. 
    If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
    Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
    """
    def reverse(self, x: int) -> int:
        # The provided NeetCode solution doesn't work, so had to use this new solution
        # Create a list, where we strip numbers from the back, and place it to the front of the list
        arr = []
        # To handle the negative stuff, we'll treat everything as positive, and just create a variable that'll flip our number negative at the end
        should_reverse = x < 0
        if should_reverse:
            x *= -1
        # Whittle down every digit until we get to the last one
        while (x // 10 > 0):
            # Find the last digit, add it to our list, and whittle down x by one more digit
            base = x % 10
            arr.append(base)
            x = x // 10
        # Add that last digit that remains
        arr.append(x)
        # Now, iteratively add each number in sum. basically, for each digit, mutiply it by it's appropriate 10^n, and add it to our running sum
        sum = 0
        for i in range(len(arr)):
            sum += ((10**(len(arr) - i - 1)) * arr[i])
        # If our number was initially negative, go ahead and multiply it by -1 now
        if should_reverse:
            sum *= -1
        # If our sum doesn't create overflow at each boundary then return the sum, otherwise return 0
        meets_constraints = -2**31 <= sum and sum <= 2**31 - 1
        return sum if meets_constraints else 0