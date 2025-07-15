class Solution:
    def isValid(self, word: str) -> bool:
        return (
            len(word) >= 3 and
            word.isalnum() and
            any(letter in "aeiouAEIOU" for letter in word) and
            any(letter.lower() in "bcdfghjklmnpqrstvwxyz" for letter in word)
        )