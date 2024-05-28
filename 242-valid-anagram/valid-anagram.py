class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def word_to_dict(word: str) -> dict:
            res = {}
            for letter in word:
                res[letter] = res.get(letter, 0) + 1
            return res
        
        return len(s) == len(t) and word_to_dict(s) == word_to_dict(t)