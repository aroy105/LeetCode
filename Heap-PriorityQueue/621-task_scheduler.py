from collections import Counter
from collections import deque
import heapq
class Solution:
    """
    Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. 
    For each unit of time, the CPU could complete either one task or just be idle.
    However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.
    Return the least number of units of times that the CPU will take to finish all the given tasks.
    """
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # General idea. First, count frequencies of an element, and place them in a MaxHeap
        # Then, run tasks in order of frequency, so more frequent elements can be run first around the less frequent elements
        # Sort the pending tasks in a queue, and only add the task back into the heap when the cooldown period ends.
        # So essentially, the heap is used for frequency, and the queue is used storing tasks that are still cooling down
        
        # Count the tasks. Counter forms a dictionary, key: value in tasks, val: freq of value in tasks
        count = Counter(tasks)
        # Create a maxHeap storing only the frequencies, as we only care about the time it takes to run the task 
        maxHeap = [-c for c in count.values()]
        heapq.heapify(maxHeap)
        
        time = 0 # Store the running time for each of the tasks
        # The queue will store the next time it can be used, along with the remaining frequency of the character
        q = deque() 
        # While there are still remaining tasks or tasks idling...
        while maxHeap or q:
            # Update the time
            time += 1 
            # If there are no available tasks
            if not maxHeap:
                # Fast forward to the time when the next available task can be done
                # The queue stores next available task, storing time it can be run + remaining frequency of unfinished tasks
                time = q[0][1]
            # If there are available tasks
            else:
                # Pop most frequent task
                # Add 1 to signify one less task of this kind needs to be done, since stored in maxHeap. 
                count = 1 + heapq.heappop(maxHeap)
                # If count is nonzero i.e. there are still remaining tasks
                if count:
                    # Add the task to the queue which stores the tasks that are still on cooldown
                    # It will be stored with the new remaining frequency and the next time it can be ran (curr time + cooldown)
                    q.append([count, time + n])
                # At this point, if if statement failed, then no need ot add to cooldown queue, since last task was run
            # While there are still tasks cooling down AND if the earliest added tasks cooldown finish matches the current time...
            if q and q[0][1] == time:
                # Add this just cooled down earliest task frequency to maxHeap
                heapq.heappush(maxHeap, q.popleft()[0])
        # Now that the while loop is finished, return the time
        return time
    
        
        