class Solution:
    """
    Write an algorithm to determine if a number n is happy.
    A happy number is a number defined by the following process:
        - Starting with any positive integer, replace the number by the sum of the squares of its digits.
        - Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
        - Those numbers for which this process ends in 1 are happy.
    Return true if n is a happy number, and false if not.
    """
    def isHappy(self, n: int) -> bool:
        # We can track each number from n to 1 (if possible) as a Linked List
        # We will use our slow/fast method, and set slow to n, and fast to the node right after n
        # Since each node one step forward is just the application of the previous node into the sumSquareDigit function
        slow, fast = n, self.sumSquareDigits(n)
        
        # Remember, this method will detect a cycle when slow = fast, since the fast node will cycle ahead and eventually catch up to the slow node from behind
        while slow != fast:
            # Increment fast by two jumps (set fast to the next node, and then set that next node to the node after)
            fast = self.sumSquareDigits(fast)
            fast = self.sumSquareDigits(fast)
            # Increment the slow pointer one node forward
            slow = self.sumSquareDigits(slow)
        
        # At this point, the slow and fast pointer have met at a node
        # If this is a happy number, then fast should be stuck at 1 when slow eventually catches up. If not, slow is at some other value, and fast caught up from behind.
        return True if fast == 1 else False
    
    
    # The following helper function just adds the sum of each digit of n
    def sumSquareDigits(self, n):
        output = 0
        while n: 
            output += ((n % 10))**2
            n = n // 10
        return output