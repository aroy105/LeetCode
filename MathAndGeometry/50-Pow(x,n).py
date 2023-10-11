class Solution:
    """Implement pow(x, n), which calculates x raised to the power n (i.e., xn)."""
    def myPow(self, x: float, n: int) -> float:
        # I'm not sure why, but for some reason, I thought only the base case value would be propogated up
        # On second look, we see when n = 1, we return x * res, where res = 1 from propogated up base case of n = 0, and x = actual value from the repeated multiplications. 
        def helper(x, n):
            # Return our base cases
            if x == 0:
                return 0
            if n == 0:
                return 1
            # Calculate the result. Note we do n // 2 since each recursive call multiples the previous value by itself
            # E.g. 2^10 -> (2*2)^5 -> ((2*2)*(2*2))^2 (truncate odd exp but from here it's always even. We handle at end of helper) = ...
            res = helper(x * x, n // 2)
            # If the exponent is odd, just return res times our base. Otherwise, return the result. This is where we pop up the chain. 
            return x * res if n % 2 else res
        
        
        # Call our helper, but only use the absolute value for the exponent. We'll turn it into a fraction and return if n < 0
        res = helper(x, abs(n))
        return res if n >= 0 else 1/res