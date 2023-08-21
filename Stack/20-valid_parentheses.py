class Solution:
    """Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid."""
    def isValid(self, s: str) -> bool:
        # The general idea is to maintain a stack where open parantheses are waiting to be matched up
        # As they get matched up, they'll be popped off
        # If s is valid, then by the end, the stack should be empty. 
        stack = []
        closeToOpen = {")":"(",
                      "}": "{",
                       "]": "["}
        for c in s:
            # If the character is a closing parenthesis
            if c in closeToOpen:
                # Make sure stack isn't empty and the top of stack is an open parenthesis
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                # invalid string (has to do with no matching open parenthesis for c)
                else:
                    return False
            # This character is an opening parenthesis, and will be added to the stack
            else:
                stack.append(c)
        # Not stack returns true if it's empty, false if it still has elements.
        return not stack