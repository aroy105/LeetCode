class Solution:
    """Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses."""
    def generateParenthesis(self, n: int) -> List[str]:
        # Approach it like a tree
        # Only add an open paranthesis if open < n
        # Only add a closing paranthesis if closed < open
        # We have a valid combo if and only if open == closed == n
        stack = []
        res = []
        
        # Recursive function that we'll use for our tree. 
        # It adds open parantheses first, then closing parantheses if open parantheses exceed it.
        # In the tree, we max out placing open parantheses, then we start adding closing parantheses. 
        def backtrack(openN, closedN):
            # Terminating condition
            if openN == closedN == n:
                res.append("".join(stack))
                return
            
            # Generic adding condition
            if openN < n:
                stack.append("(")
                backtrack(openN+1, closedN)
                stack.pop()
                
            # Generic closing condition
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN+1)
                stack.pop()
        
        backtrack(0, 0)
        return res