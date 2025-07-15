class Solution:
    def isValid(self, word: str) -> bool:
        return (
            len(word) >= 3 and
            all(letter in "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789" for letter in word) and
            any(letter in "aeiouAEIOU" for letter in word) and
            any(letter not in "aeiouAEIOU" and letter.isalpha() for letter in word)
        )