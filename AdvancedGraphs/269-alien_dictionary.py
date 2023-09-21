class Solution:
    """
    There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you.
    You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. 
    Derive the order of letters in this language.
    1. You may assume all letters are in lowercase.
    2. The dictionary is invalid, if string a is prefix of string b, and b appears before a. 
    3. If the order is invalid, return an empty string.
    4. There may be multiple valid order of letters, return the smallest in normal lexicographical order.
    5. The letters in one string are of the same rank by default and are sorted in Human dictionary order.
    """
    def alienOrder(self, words: List[str]) -> str:
        # As we create and figure out the ordering in the alient language, we can create graph subsections, such as letter X -> letter Y
        # Different orderings come up, like X -> Y, Z -> B, B -> A, and thus, we just created new graph subsections, like so...
        # X -> Y, Z -> B -> A. 
        # Eventually, these graph subsections can eventually became one long chain, and this chain can be returned as the solution, since it is in order
        # However, if a cycle exists, then we know that no ordering exists i.e invalid solution
        # We will use something called topological sort to go and order this, which is where every node is visited only after all it's dependencies are visited. 
        # A topological ordering is possible if and only if the graph has no directed cycle i.e. a directed acyclic graph (DAG)
        # Time: O(# of letters)
        # Space: O(V + E)
        characterGraph = {character: set() for word in words for character in word}
        
        # Compare every pair in words, so i and i + 1, hence the unqiue range below
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1] # Store the first and second word of the pair
            minLength = min(len(w1), len(w2)) # Collect the size of the smaller word
            # Base Case 2 (see question) where the longer letter is ahead of the smaller letter, when they're both equal for each letter. Return ""
            if len(w1) > len(w2) and w1[:minLength] == w2[:minLength]: 
                return ""
            # Compare each letter index-wise, and at the first difference i.e. we found a new ordering pattern, add it to the character Graph. 
            for j in range(minLength):
                if w1[j] != w2[j]:
                    characterGraph[w1[j]].add(w2[j])
                    # At first I was confused why we break, but the reason why is because we can't find any new patterns after the first difference. In hindsight this is obvious
                    # I.e. Assume two words "eg" and "ge" with normal human ordering. From first index, we see e->g, but if we examined second index, it would show g->e
                    # So we obviously don't care about comparing any indices after the first difference
                    break
        
        visited = {}
        res = []
        # We're going to use a DFS approach here to check for cycles and add letters, since there's less bookkeeping than if we used BFS
        def isCycle(character):
            # If we have already visited the character, see if it was as a part of our current ordering chain that we are checking (i.e. check if there's a cycle)
            if character in visited:
                return visited[character]
            # At this point, it wasn't visited, so add it to our visited stack
            visited[character] = True
            # Now, run DFS down every lower-ordered character below this current character
            for neighbor in characterGraph[character]:
                if isCycle(neighbor):
                    return True
            # At this point, no cycles were detected going down any of the lower added characters, so we can go ahead and it to our cycle. 
            # We also ended this "chain" of ordering, so we have visited the character, but it's no longer a part of chain being currently checked, so set it to False
            visited[character] = False
            res.append(character)
            # Indicate no cycles were found down this character or the characters it's above
            return False
        # Go through every character 
        # For the lexographical ordering, LintCode uses "for c in sorted(charGraph.keys(), reverse=True)" instead
        for c in characterGraph:
            # If a cycle is detected, we no longer have a DAG, and we found a ordering where a previously higher ordered letter is now lower than a previously lower ordered letter
            # This is obviously wrong, so return ""
            if isCycle(c):
                return ""
        # Remember, at this point, we added our characters from the top of the recursive stack to the bottom i.e. the lowest ordered letters
        res.reverse()
        return "".join(res)

# So I used to be confused why it could be started at any point, and I think it's because we have a DAG
# My concern was that essentially, what if the first character we go through is not the highest ordered one. 
# But I think because it's a DAG, it's impossible for us to fully go through one path, and then we "forget" to place some elements in between others
# Basically, because there are multiple valid orderings, we can always assume that two nodes, who's orderings may be ambiguous like a -> b <- c can be ordered as both acb or abc. 
# LintCode specifies that if this happens, then go with abc. 
# With DAGs, once we go down one route, you examine everything under it. 
# We've already graphed all connections, and by going through the adjacency list, we go all the way down and hit all the connections, and miss nothing. 
# Other things that aren't in that chain are ambiguously defined, so as long as they're above the things they're directly defined above, any ordering works.
