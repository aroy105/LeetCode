class Solution:
    """Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings."""
    def encode(self, strs):
        # We need to pick something unique that will help us later decode the string, but our solution must be stateless

        # One solution is to prepend each str with 'len(str)#', where # is a unique delimiter. 
        # One confusion that I had was what if our string starts with some random number followed by a #. 
        # This concern is bypassed by the fact that once we extract the length of the string, we immediately break that part off, and jump to the next 'len(str)#'
        # Since the very first characters of the encoded string are 'len(str)#', we never run into a situation where we acidentally take in something as an instruction
        res = ""
        for s in strs:
            res += str(len(s) + "#" + s)
        return res
        
    def decode(self, s):
        res, i = [], 0

        # i will track the starting point of our current string
        while i < len(s):
            # Create a temporary pointer that tracks the end point of our current string. 
            j = i
            # In case the length of the current string is multiple digits long...
            while s[j] != "#":
                j += 1
            # s[i:j] is the length of the string, so turn it into an int and store the value
            length = int(s[i:j])
            res.append(s[j + 1: j + 1 + length])
            
            i = j + 1 + length
        
        return res
