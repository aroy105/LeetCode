class Solution:
    """You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation. Evaluate the expression."""
    def evalRPN(self, tokens: List[str]) -> int:
        # Add numbers to the stack. If an operator comes up, pop the two top values, evaluate the answer, and append the result to the stack.
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(c))
        return stack[0]