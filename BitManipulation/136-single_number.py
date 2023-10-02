class Solution:
    """
    Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
    You must implement a solution with a linear runtime complexity and use only constant extra space.
    """
    def singleNumber(self, nums: List[int]) -> int:
        # We can repeatedly XOR all the numbers together, and our output should be the remaining number
        # We will basically have result = number1 ^ number1_duplicate ^ number2 ^ number2_duplicate ^ ... ^ unique_number
        # Remember, Boolean logic is commutative, so the result from grouping our nums array as such is identical to whatever they were originally organized as
        # This means we can just iterate through the for loop, and XOR our running result with the next number
        # Back to the equation, A XOR A = 0, so all the duplicate expressions (number_x ^ number_x_duplicate) = 0 
        # We will then be left with result = 0 ^ unique number. From our truth table, we know 0 XOR 0 = 0, and 0 XOR 1 = 1. 
        # Thus, for each digit, if the unique number has a 0 there, the corresponding digit in the result will also be zero, and if there's a 1, the output will still be 1
        # In other words, if the placement of 0's and 1's are intact, 0 XOR unique_number just outputs the unique number! So result = 0 ^ unique_number = unique_number
        
        # We create a blank global variable for result. Remember, 0 ^ A = A, so doing 0 ^ A_1 ^ A_2 ^ ... = A_1 ^ A_2 ^ ...
        result = 0
        # Take the XOR of every single number in our list, and return the unique value
        for n in nums:
            result = result ^ n
        return result
        