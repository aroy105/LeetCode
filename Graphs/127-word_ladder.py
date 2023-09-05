import collections
class Solution:
    """
    A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
        - Every adjacent pair of words differs by a single letter.
        - Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList. 
        - sk == endWord
    Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.
    """
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # We can create a graph, which links the words in wordlist to all the other words in wordlist that differ with it by 1 character. 
        # Then, we can rapidly return the shortest path from begin to end word. 
        # Building this list is the tricky part though, as the naive approach doesn't pass on LeetCode
        
        if endWord not in wordList: # Base case
            return 0
        
        # Create a kind of adjacency list called neighbors
        neighbors = collections.defaultdict(list)
        # Add our starting word to wordList, so we can include it in our adjacency list
        wordList.append(beginWord)
        # For each word
        for word in wordList:
            # Go through every letter in the word, and create a pattern where essentially it's a wild character now
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1 :]
                # With this pattern as the key, add the word as the value i.e. neighbors["foob*r"] = ["foobar", "foobur", "foobnr"]
                neighbors[pattern].append(word)
        
        # We don't want to revisit the same position twice, and we want to start at the beginning word
        visit = set([beginWord])
        # Run BFS
        # We start with the beginning word, and then go one letter changes at a time, until we find the shortest path
        q = collections.deque([beginWord])
        # This indicates the length of the chain. Set it to 1 to indicate the first word, beginWord
        res = 1
        # While neighbors exist in the deque
        while q:
            # For each neighboring word
            for i in range(len(q)):
                word = q.popleft()
                # If the word is the end word, return the chain
                if word == endWord:
                    return res
                # For each letter in the word, generate a pattern
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1 :]
                    # For each of the similar words that correspond to the pattern
                    for neighborWord in neighbors[pattern]:
                        # If we haven't visited yet, add it to visit, and then add it to our deque for future examination
                        if neighborWord not in visit:
                            visit.add(neighborWord)
                            q.append(neighborWord)
            # Now that we are moving to the next layer, increment our count
            res += 1
        # At this point, no path was found, and thus, no way exists
        return 0
            