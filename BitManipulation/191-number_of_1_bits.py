class Solution:
    """
    Write a function that takes the binary representation of an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).
    Note:
    Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input will be given as a signed integer type. 
    It should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
    In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3, the input represents the signed integer.
    """
    def hammingWeight(self, n: int) -> int:
        # One solution is to go through every digit, and mod the digit by 2. If it ends in 0, mod 2 will return 0, if it ends in 1, mod 2 will return 1, similar to even or odd things
        # result = 0
        # while n: # n != 0
        #     result += n % 2
        #     n = n >> 1 # This just bitshifts it to the right
        # return result
        
        # This is the more complicated solution, that basically jumps every zero bit, so is slightly faster
        
        res = 0 
        # Every time this while loop runs, we basically ran into a '1', so we increment result
        while n:
            # Look at the case of n = 1000001. n - 1 = 10000000, so n & n-1 = 10000000
            # In the next step, n = 10000000, n-1 = 01111111, so n & (n-1) = 00000000. At this point, the program terminates.
            # Think about this. In the first step, we basically lopped off the right-most 1, and in the second step, we knocked out the last remaining '1'
            # Subtracting 1 from n basically flips all the digits up to the right most 1. Even if the '1' isn't the left-most digit, the carryover flips all the prior 0's to 1's in n-1
            # So when we evaluate n & (n-1), all the digits for both numbers match up until that left most 1
            # I.e. n = 1000 1000, so n-1 = 1000 0111. Then, n & (n - 1) = 1000 0000. 
            
            n = n & (n - 1) # Can be abbreviated as n &= (n-1)
            
            # Since we've lopped off a single 1, we only need to increment our result by 1. 
            res += 1
        return res