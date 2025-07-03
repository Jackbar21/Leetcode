class Solution:
    def kthCharacter(self, k: int) -> str:
        word = "a"
        getNextLetter = lambda letter: "a" if letter == "z" else chr(ord(letter) + 1)
        while len(word) < k:
            word += "".join(map(getNextLetter, word))
        return word[k - 1]