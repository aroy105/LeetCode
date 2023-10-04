class Solution:
    """
    You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
    The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
    Increment the large integer by one and return the resulting array of digits.
    """
    def plusOne(self, digits: List[int]) -> List[int]:
        # This is the "plus one" that we're adding to our integer, and i is the current 'digit' we're looking at
        one, i = 1, 0
        # Reverse our digits, so that going from the front to the back of the number means going from the least to most significant digit
        digits = digits[::-1]
        # one will also be used to represent 'carry-in' to the current digit. So while we still have a carryover, we need to keep adding stuff
        while one:
            # If we haven't gone out of bounds of the array i.e. we don't need a new space in the array
            if i < len(digits):
                # If our digit is 9 i.e. 9 + 1 = 10, clear the digit and preseve the carryout. Otherwise, add the carry-in to the current digit, and clear the carry-in
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    one = 0
            # If we now do need to go out of bounds, add the carry-in, and clear the value once added
            else:
                digits.append(one)
                one = 0
            # Increment our digit pointer, to point to the next digit
            i += 1
                
        # Reverse our digits again
        return digits[::-1]