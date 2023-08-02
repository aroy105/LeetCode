from collections import defaultdict, Counter
class Solution:
    """
    Given an m x n grid of characters board and a string word, return true if word exists in the grid.
    The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. 
    The same letter cell may not be used more than once.
    """
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Just to a brute force DFS approach to solve this. Will be O(n*m*4^n)
        ROWS, COLS = len(board), len(board[0])
        # We will keep track of the path we take in a set, so we don't revisit already traversed coordinates
        path = set()
        
        def dfs(r, c, i):
            # If we have found the word...
            if i == len(word):
                return True 
            # If either r/c is out of bounds, if the board letter doesn't match our word, or if the current coordinate was already previously traversed...
            if (
                min(r, c) < 0 # out of bounds, where if either r or c is negative, return false
                or r >= ROWS or c >= COLS # Out of bounds for if they're higher
                or word[i] != board[r][c] # board letter != word letter
                or (r, c) in path # board square already in path
                ):
                return False 
            
            # At this point, we have found a square that is eligible and matches the next letter of our word 
            # Record it's position in the path 
            path.add((r, c))
            # Recursively check right, left, up, and down respectively, and see if any of those yield a valid word. If any path is true, word exists. Else false. 
            res = (
                dfs(r + 1, c, i + 1)
                or dfs(r - 1, c, i + 1)
                or dfs(r, c + 1, i + 1)
                or dfs(r, c - 1, i + 1)
            )
            # Disassemble path for recursive steps, so future recursions have the proper path
            path.remove((r, c))
            return res
        
        # This next step is a little optimization (feels kinda hacky imo). 
        # In this algo, we essentially run DFS on each square, and compare against each letter. Now how can we find a answer quicker? 
        # First, find the frequency of each letter. Then check the frequency of the first and last letter on the board. 
        # If the first letter is more frequent, we can reverse our word, and then run the algo. 
        # If the new word is now reversed, it starts with a less frequent character, meaning we can quickly reject most of the stuff we come across. 
        # Since most of our path space will be rejected, the quicker we can burn through them and find a correct answer, the faster we will be
        # The path is preserved and nothing is essentially changed by reversing the word. 
        
        # First, find frequency of each word, and store it as a dictionary in count
        # This is complicated, so I will explain each part. map works like map(function, iterable)
        # So map(Counter, board) creates a list of Counter objects to each element in board. These Counter objects behave like dictionaries
        # sum(map(Counter, board), Counter()) adds up all the counts in Counter objects across board,
        # the second Counter() provides an empty counter to start the sum. 
        # Finally, in defaultdict, the int means we default to 0, and if you try to access a key that doesn't exist, it returns 0.
        
        count = defaultdict(int, sum(map(Counter, board), Counter()))
        # Check frequency of first and last word. If first letter is more frequent, reverse the word
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]
        
        # Brute force across whole space
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True 
        # If we checked everything, return False. 
        return False