class Solution:
    """
    Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.
    The following rules define a valid string:
        - Any left parenthesis '(' must have a corresponding right parenthesis ')'.
        - Any right parenthesis ')' must have a corresponding left parenthesis '('.
        - Left parenthesis '(' must go before the corresponding right parenthesis ')'.
        - '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
    """
    def checkValidString(self, s: str) -> bool:
        # These values represent the minimum and maximum open left parantheses we could have
        leftMin, leftMax = 0, 0
        # For each character in the string...
        for c in s:
            # A new left parantheses would increment both values
            if c == "(":
                leftMin, leftMax = leftMin + 1, leftMax + 1
            # A new right parantheses would decrement both values, as it closes the open parantheses
            elif c == ")":
                leftMin, leftMax = leftMin - 1, leftMax - 1
            # If we get a wild character, it could either be a closing parantheses (leftMin - 1) or a new open parantheses (leftMax + 1)
            else:
                leftMin, leftMax = leftMin - 1, leftMax + 1
            # The leftmax should always be at least zero, there are too many closing parantheses if it is less than that
            if leftMax < 0:
                return False
            # There may be a leftMin which is less than 0, since theoretically some of those wildcards would be just turned into ""
            if leftMin < 0:  
                leftMin = 0 # Set it to zero since we could have a proper configuration like that
        # If leftMin is not zero at this point, that means there were too many opening left parantheses.
        return leftMin == 0