class Solution:
    """
    Given a signed 32-bit integer x, return x with its digits reversed. 
    If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
    Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
    """
    def reverse(self, x: int) -> int:
        # Our basic process will be to snip off numbers from the 0th to the 32nd bit, pad the zeros necessary, and then add it to our result from the 32nd bit to the 0th bit
        
        # This will be our starting bit for our result
        result = 0
        # Go through every bit from the start to the end
        for i in range(32):
            # This will be the bit we're currently transcribing. x >> i shifts it to the right by i bits, getting the ith MSB, and b & 1 stores a 1 if b is also 1. Otherwise, it just records 0
            # It will first be 
            bit = (x >> i) & 1
            # We then leftshift by (32-i) bits, padding it with that many zeros from the right, and add it to our result
            result += (bit << (31 - i))
        
        return result