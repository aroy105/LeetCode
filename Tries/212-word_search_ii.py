class Solution:
    """
    Given an m x n board of characters and a list of strings words, return all words on the board.
    Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring.
    The same letter cell may not be used more than once in a word.
    """
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Create a root trie node
        root = TrieNode()
        # for each word, add the word into the Trie
        for w in words:
            root.addWord(w)

        ROWS, COLS = len(board), len(board[0])
        # Create results and visited set, visit helps us to not get stuck in a loop
        res, visit = set(), set()
        # Run DFS on each letter
        def dfs(r, c, node, word):
            # Base cases for termination, like out of bounds, does not exist, already visited
            if (
                r not in range(ROWS) 
                or c not in range(COLS)
                or board[r][c] not in node.children
                or node.children[board[r][c]].refs < 1
                or (r, c) in visit
            ):
                return
            # Add current coordinate to visit set
            visit.add((r, c))
            # Update node pointer
            node = node.children[board[r][c]]
            # Update word given character we just reached
            word += board[r][c]
            # If this new character is at the end of the word, add it to results and remove it from the board
            if node.isWord:
                node.isWord = False
                res.add(word)
                root.removeWord(word)
            # Do dfs in all four directions
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            # once we've gone in all directions, remove the current location, as it may be a part of new words.
            visit.remove((r, c))
        
        # Go through each entry in the board, and run dfs
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
        # Return our set as a list
        return list(res)

# NEED TO MAKE A NEW CLASS CALLED A TRIE NODE
class TrieNode:
    def __init__(self):
        # Representing one of 26 possible future children letters
        self.children = {}
        # See if this node is an ending
        self.isWord = False
        self.refs = 0
        
    def addWord(self, word):
        cur = self # This sets it to the root node
        cur.refs += 1 
        # Go through each letter and if it isn't in the trie, add it.
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            # Push the pointer down
            cur = cur.children[c]
            cur.refs += 1 
        # Once you've gone through all the letters, mark the node as the end of a word
        cur.isWord = True
        
    def removeWord(self, word):
        # Set pointer to root node
        cur = self 
        cur.refs -= 1 
        # Go through each letter in the word, and decrement the refs variable. 
        # If cur.refs > 0, it is still a "valid" node
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
                cur.refs -= 1 
                