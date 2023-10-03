class Solution:
    """Given two integers a and b, return the sum of the two integers without using the operators + and -."""
    def getSum(self, a: int, b: int) -> int:
        # Essentially, we notice that XOR is remarkably similar to addition, but it can't handle the carryout 
        # We could just take the resulting a ^ b, and then "add" this (XOR) with all the carryouts. These carryouts can be represented as a string
        # But how do we generate a carryout string? Well, we have a carryout when both the bit in a and b are 1, so we can use AND to create a carryout string
        # However, this will create 1's at the index instead of the next index, which is where the carryout occurs. So we need to bitshift (A & B) to the left one space
        # Then, we can just do (a & b) ^ (a ^ b). However, this outer XOR operation may also yield carryouts, so we basically repeat this until cout = 0
        
        # Due to the silly goose way Python handles 32 bit integers, the answer is more intuitive in Java, which is shown all the way at the end of the file
        def add(a, b):
            # If either a or b is zero, just return the one which is not negative. If both are negative, still returns 0
            if not a or not b:
                return a or b
            # Otherwise, just recursively add a and b sans carryout, and then add the carryout
            return add(a ^ b, (a & b) << 1)

        # If one is negative and one is positive, we need to take some special precautions
        if a * b < 0:
            # We will always treat a as the negative one. The next two lines basically force switch a and b and restart the function, so that the a parameter is the negative one, and b is positive
            if a > 0:
                return self.getSum(b, a)
            # add(~a, 1) is a way we can represent -a. If we were to just use ~a, I think it would do 2's Complement stuff, and give a number off by 1.
            # If -a == b, then the addition of a + b = a - a = 0.
            if add(~a, 1) == b:
                return 0
            # If -a < b, then just return -add(-a, -b). Again, can't directly use ~a unfortunately
            if add(~a, 1) < b:
                return add(~add(add(~a, 1), add(~b, 1)), 1)
        # if both a and b are positive or both are negative, just return 
        return add(a, b)

# class Solution {
#     public int getSum(int a, int b) {
#         # We use a to hold the result, and b to store carryouts
#         # This way, we can just iterate until the carryout is zero
#         while (b != 0) {
#             # We need to change a and b only after we use them, so store the carryout in temp, calculate the a XOR b, then set a to this, and assign b as the carryout
#             int tmp = (a & b) << 1;
#             a = (a ^ b);
#             b = tmp;
#         }
#         # a always had the sum, so return it
#         return a;
#     }
# }
