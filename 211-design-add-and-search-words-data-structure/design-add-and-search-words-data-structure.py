class WordDictionary:
    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        trie = self.trie
        for letter in word:
            if letter not in trie:
                trie[letter] = {}
            trie = trie[letter]
        trie[","] = () # INTENTIONALLY EMPTY!!!
        
    def search(self, word: str) -> bool:
        return self.searchWord(word, 0, self.trie)

    def searchWord(self, word, i, trie):
        if i >= len(word):
            assert i == len(word)
            return "," in trie
        
        letter = word[i]
        if letter != ".":
            if letter not in trie:
                return False
            return self.searchWord(word, i + 1, trie[letter])
        
        assert letter == "."
        for key in trie:
            if self.searchWord(word, i + 1, trie[key]):
                return True
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)