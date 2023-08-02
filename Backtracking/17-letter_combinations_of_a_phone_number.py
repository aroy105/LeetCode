class Solution:
    """
    Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
    A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
    """
    def letterCombinations(self, digits: str) -> List[str]:
        # Basically, you need to create new branches for each new letter, and slowly build out words from there
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        def backtrack(i, curStr):
            # Base case if the length of the saved string is as big as the input string, save the answer
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            # Create a branch for each corresponding letter we could choose. We use our hardcoded dictionary to determine what branches each digit corresponds to
            for c in digitToChar[digits[i]]:
                # Update the pointer, append the chosen branch's letter to the running string we have built
                backtrack(i + 1, curStr + c)
        
        # If the input isn't null, run backtracking. Then return the result. 
        if digits:
            backtrack(0, "")
        return res