class Solution:
    """
    Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
    Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
    """
    def multiply(self, num1: str, num2: str) -> str:
        # THIS SOLUTION IS VERY SLOW AND MEMORY INTENSIVE COMPARED TO OTHERS ON LEETCODE
        
        # If either value is zero, return 0 since 0 * any number is 0
        if "0" in [num1, num2]:
            return "0"
        
        # create a list for our result. Note, the length of the product of 2 numbers is always at most the sum of the number of digits they have
        # for example, if we try to max out a digit number by a one digit number i.e. 9*9, we get 81, which as expected is two digits
        res = [0] * (len(num1) + len(num2))
        # Reverse the strings, so we start from the one's digit to the most significant digit
        num1, num2 = num1[::-1], num2[::-1]
        # now just do multiplication haha, by multiplying each digit with every other digit in the other number
        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                # Calculate the product of two places
                digit = int(num1[i1]) * int(num2[i2])
                # Add this product to whatever is currently in the spot it should be in. Remember, the location will be the sum of the index pointers. 
                res[i1 + i2] += digit
                # Add whatever carryover would belong in the next spot
                res[i1 + i2 + 1] += res[i1 + i2] // 10
                # Since the carryout has already been done, just retain the one's digit in the index needed
                res[i1 + i2] = res[i1 + i2] % 10
        
        # Reverse our result list, and create a pointer at the most significant digit
        res, beg = res[::-1], 0
        # While the pointer has not crossed past the ones digit and the most significant digit is zero, push the pointer back
        while beg < len(res) and res[beg] == 0:
            beg += 1
        # Basically, this just skips the extra zeros that may exist at the front of our number. 
        # Then, basically truncate all the digits except the leading zeros, and map them to a strings. Return the result of stringing them all up together
        res = map(str, res[beg:])
        return "".join(res)