class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split(" ")
        brokenLetters = set(brokenLetters)
        res = len(words)
        for word in words:
            for letter in word:
                if letter in brokenLetters:
                    res -= 1
                    break
        return res