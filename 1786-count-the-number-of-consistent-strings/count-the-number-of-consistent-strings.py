class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_letters = set(allowed)
        # return len(list(
        #     filter(lambda word: all([letter in allowed_letters for letter in word]), words)
        # ))
        
        res = 0
        for word in words:
            is_allowed = True
            for letter in word:
                if letter not in allowed_letters:
                    is_allowed = False
                    break
                
            res += is_allowed
        
        return res