class TimeMap:
    """
    Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.
    Implement the TimeMap class:
    TimeMap() Initializes the object of the data structure.
    void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
    String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. 
    If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".
    """
    def __init__(self):
        # We will have a hashmap where the value is a list of [val, timestamp]
        self.keyStore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # If the key doesn't exist create it
        if key not in self.keyStore:
            self.keyStore[key] = []
        # At this point the key exists. Now just append to the end of the list
        self.keyStore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        # Default value for if we don't find the key is ""
        # I was stupid and I got confused here. I forgot that get is a dictionary function, where answer = get(key for answer, default value if key is not in dictionary)
        # I thought we were doing recursive voodoo with the TimeMap class help method. That would be self.get, not just .get, and it wouldn't be associated with the dictionary
        res, values = "", self.keyStore.get(key, [])
        # Now we can do a binary search on our data structure
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            # Remember, values[m][1] is the timestamp
            if values[m][1] <= timestamp:
                # since this is a valid min solution, store it, and push right
                res = values[m][0]
                l = m + 1
            else:
                # Invalid solution, ignore all values to the right of this, since the timestamps can only be greater towards the right (time is linear lol)
                r = m - 1
        return res