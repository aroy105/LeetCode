class WordDictionary:
    """Design a data structure that supports adding new words and finding if a string matches any previously added string."""
    def __init__(self):
        """Initializes the object"""
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """Adds word to the data structure, it can be matched later."""
        # Set pointer to top of trie
        cur = self.root 
        # Iterate through each word
        for c in word:
            # If corresponding TrieNode child doesn't exist for word, add it
            if c not in cur.children:
                cur.children[c] = TrieNode()
            # Update pointer
            cur = cur.children[c]
        # Set the current TrieNode's self.word variable to true, to signify the end of a word after iterating through all values
        cur.word = True

    def search(self, word: str) -> bool:
        """
        Returns true if there is any string in the data structure that matches word or false otherwise. 
        word may contain dots '.' where dots can be matched with any letter.
        """
        # Use dfs to go through all existing words
        def dfs(j, root):
            # Set pointer to top of trie
            cur = root 
            # Go through each letter in our specified substring, initially set to the whole word. Can be shorter given "."
            for i in range(j, len(word)):
                
                c = word[i]
                # If we have a placeholder
                if c == ".":
                    # We need to go through every possible subtree from here, so recursively run dfs through all the children, starting from the current letter
                    for child in cur.children.values():
                        # At the child, run dfs, with i + 1 since it is the next letter in the word
                        if dfs(i + 1, child):
                            return True 
                    # At this point, we must have not found a matching child. 
                    return False 
                # If the current character is not "."
                else:
                    # If the current character doesn't exist among the children of the previous node, return false. Otherwise, update pointer
                    if c not in cur.children:
                        return False 
                    cur = cur.children[c] 
            # At this point, we have gone through the length of the entire word. Now we must check if a previously inserted word ended at the current node, so return this truth value. 
            return cur.word 
        # Return the solution to dfs at the top of the trie starting from the first word. 
        return dfs(0, self.root)
                

# HAVE TO MAKE CLASS FOR EACH OF THE TRIENODES
class TrieNode:
    def __init__(self):
        self.children = {} # individually index new words, like 'a' : TrieNode
        self.word = False