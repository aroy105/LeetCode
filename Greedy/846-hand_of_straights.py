import heapq
class Solution:
    """
    Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.
    Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.
    """
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # If we can't even make all the groupings given the hands, just return false
        if len(hand) % groupSize:
            return False
        # We'll use a dictionary to store the count of each element 
        count = {}
        for n in hand:
            count[n] = 1 + count.get(n, 0)
        
        # We will then make a minheap of all the instances of the card (not storing repeats)
        minH = list(count.keys())
        heapq.heapify(minH)
        
        # While there are still elements on our heap
        while minH:
            # Here is a general idea. 
            # If you have a small value, like 1, it can only be grouped with higher values, since no '0' card exists
            # Thus, we always start groupings from the lowest element
            first = minH[0]
            # For all the cards in the group....
            for i in range(first, first + groupSize):
                # If the next sequential card doesn't exist e.g. first = 3, but no 4 card exists, return False
                if i not in count:
                    return False 
                # indicate the card has been added to the group, and reduce the count by 1
                count[i] -= 1
                # When no more cards of this type exist, the card needs to be popped from our minHeap as well
                if count[i] == 0:
                    # If the value we're trying to pop is not the minimum value, then that means it still exists lower in the minHeap
                    # This confused me at first, but basically, up til here, we've removed all values (including prior minHeap), if only one instance occurs
                    # If the card we're trying to remove is not the lowest remaining value in the cards we are left to use, something wrong has happened
                    # This is because if this card is getting removed while smaller values exist, how can groupings be made for the future smaller values?
                    # That means we don't have enough of future consecutive values in the next iteration of while minH. So we can return false
                    if i != minH[0]:
                        return False
                    # At this point, it is safe to permanently pop the value
                    heapq.heappop(minH)
        # At this point, all valid groupings were made.
        return True
            