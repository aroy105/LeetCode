class MinStack:
    """
    Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

    Implement the MinStack class:

    MinStack() initializes the stack object.
    void push(int val) pushes the element val onto the stack.
    void pop() removes the element on the top of the stack.
    int top() gets the top element of the stack.
    int getMin() retrieves the minimum element in the stack.
    You must implement a solution with O(1) time complexity for each function.
    """
    # Essentially, our implementation will store tuples, where the first index stores the value, and the second index stores the min value at that point
    def __init__(self):
        self.stack = []
    # Create the tuple and push it. 
    # The tuple's min value is min(current value, previous tuple's min), but if it's the first value, then min value is just set to value. 
    def push(self, val: int) -> None:
        self.stack.append((val, min(val, self.stack[-1][1] if self.stack else val)))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0] if self.stack else None

    def getMin(self) -> int:
        return self.stack[-1][1] if self.stack else None