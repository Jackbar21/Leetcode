class Solution:
    def isValid(self, word: str) -> bool:
        return (
            len(word) >= 3 and
            word.isalnum() and
            any(letter in "aeiouAEIOU" for letter in word) and
            any(letter not in "aeiouAEIOU" and letter.isalpha() for letter in word)
        )