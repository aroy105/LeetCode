class Solution:
    """
    You are climbing a staircase. It takes n steps to reach the top.
    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
    """
    def climbStairs(self, n: int) -> int:
        # If steps = 1, only 1 way, if steps = 2, only {1 + 1, 2}, if steps = 3, {1+1+1, 1+2, 2+1}
        if n <= 3:
            return n
        # This will always be the case, where crossing two steps can be done in two ways, and three steps in three ways
        # This is like our base case, everything else gets built up from this
        # n1 is like f_n-1, n2 is like f_n
        n1, n2 = 2, 3
        
        # Now, we build up our cases, and consider higher step numbers. For every step higher than our base cases...
        for i in range(4, n+1):
            # If we add a step, we can either jump one or two steps forward
            # Imagine we were at three steps, and now we have to traverse four. We are at Step 4
            # One hop takes us to step 3, and we know from base cases there are three ways we can get to the end from there
            # A two-step hop takes us to step 2, and we know from bases cases there are two ways we can get to the end from there
            # Thus, standing at step 4, there are 5 ways we can get to end. 
            
            # However, we need to update our f_n-1 and f_n values for the next step, so push n1 to the current "next step" i.e. n2, and update n2. 
            # We need a temp variable to accomplish this
            temp = n1 + n2
            n1 = n2
            n2 = temp
        # Return our current step
        return n2