class LRUCache:
    """
    Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
    Implement the LRUCache class:
    LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
    int get(int key) Return the value of the key if the key exists, otherwise return -1.
    void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
    The functions get and put must each run in O(1) average time complexity.
    """
    
    # Basically we can create a hashmap that has keys pointing to our actual nodes, with two pointers for least and most recently used
    # REMEMBER THAT AT THE BOTTOM WE HAD TO CREATE OUR OWN NODE CLASS FOR DOUBLY LINKED LIST IMPLEMENTATION. 
    
    def __init__(self, capacity: int):
        # Create the LRUCache
        self.cap = capacity
        self.cache = {}
        # Create the LRU and MRU pointers, set them to dummy nodes, and have them point to each other
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
        

    def get(self, key: int) -> int:
        if key in self.cache:
            # Now that we got it, we want it to be the Most Recently Used one 
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            # Return the desired one
            return self.cache[key].val
        return -1 # Problem asks us to do this if it doesn't exist

    def put(self, key: int, value: int) -> None:
        # If it already exists, remove it's old instance. 
        if key in self.cache:
            self.remove(self.cache[key])
        # Create and insert a new instance where we want it
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        # If adding something made it too big, we now need to evict LRU node, deleting it from the cache and the hashmap
        if len(self.cache) > self.cap:
            lru = self.left.next 
            self.remove(lru)
            del self.cache[lru.key]
    
    # HELPER FUNCTIONS FOR CODE
    
    def remove(self, node):
        """Remove from list"""
        prev, next = node.prev, node.next 
        prev.next, next.prev = next, prev
        
        
    def insert(self, node):
        """Insert node at current position of right most pointer (between previous and right pointer)"""
        prev, next = self.right.prev, self.right
        prev.next = next.prev = node
        node.prev, node.next = prev, next 


# THIS IS THE FIRST STEP, TO MAKE THE NODE
class Node:
    """Doubly Linked List Design"""
    def __init__(self, key, val):
        self.key, self.val = key, val 
        self.prev = self.next = None
        