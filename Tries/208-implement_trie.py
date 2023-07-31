class Trie:
    """
    A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. 
    There are various applications of this data structure, such as autocomplete and spellchecker.
    """
    def __init__(self):
        """Initializes the trie object."""
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """Inserts the string word into the trie."""
        # Set current pointer to the root 
        curr = self.root
        # We need to iterate through each char in word, to see if there are existing branches we can build off/if the word exists.
        for c in word:
            i = ord(c) - ord("a") # Quickly helps check the index of where the character should be if the word already exists
            # If our current character is not an existing child, it means we haven't inserted this word yet
            if curr.children[i] == None:
                curr.children[i] = TrieNode()
            # Set the curr pointer to the current letter
            curr = curr.children[i]
        # After we have gone through all the children, this means a letter has terminated, so mark it as the end of a word
        curr.end = True

    def search(self, word: str) -> bool:
        """Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise."""
        ##### POSSIBLE BUG, WHAT IF SEARCH WORD IS LARGER THAN ANY OTHER PREVIOUSLY ENTERED NODE?
        # Set pointer to top of trie
        curr = self.root 
        # Iterate through each letter
        for c in word:
            # If current letter is not an existing child, the letter must not be here
            i = ord(c) - ord("a")
            if curr.children[i] == None:
                return False
            # Update pointer
            curr = curr.children[i]
        # We are now at the trie node where our word supposedly ends, so we check the node to see if any previously inserted word ended here.  
        return curr.end

    def startsWith(self, prefix: str) -> bool:
        """Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise."""
        # Start at top of trie, iterate through each char in prefix
        curr = self.root 
        for c in prefix:
            # If a current character does not exist as a possible child of the previous TrieNode, return false
            i = ord(c) - ord("a")
            if curr.children[i] == None:
                return False 
            # Update pointer
            curr = curr.children[i]
        # By this point, all TrieNodes must have matched up with prefix letters. 
        return True
        

# NEED TO MAKE A NEW CLASS CALLED A TRIE NODE
class TrieNode:
    def __init__(self):
        # Representing one of 26 possible future children letters
        self.children = [None]*26
        # See if this node is an ending
        self.end = False