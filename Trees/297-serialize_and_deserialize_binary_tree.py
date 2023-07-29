class Codec:
    """
    Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
    Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. 
    You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.
    Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.
    """
    # We will record it as a preorder traversal
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # Where we will store our vals
        res = []
        
        def dfs(node):
            # When we hit a null child
            if not node:
                res.append("N")
                return
            # Add value
            res.append(str(node.val))
            # Recursively go down the left and right
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        # use "," as a delimiter for all the values
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(",")
        # Since we are in a class, self.i lets us make a global variable for the pointer in our list
        self.i = 0
        
        def dfs():
            # We encounter a null child, so go to next value in vals, and return None
            if vals[self.i] == "N":
                self.i += 1 
                return None 
            # Make a node for the current value if not null, move the list pointer up one
            node = TreeNode(int(vals[self.i]))
            self.i += 1 
            # Recursively call dfs on the left and right subtrees of the current node
            node.left = dfs()
            node.right = dfs()
            # Return the node we made for this current one
            return node
        # Return the root of this tree, since we start at self.i = 0.
        return dfs()
            
        