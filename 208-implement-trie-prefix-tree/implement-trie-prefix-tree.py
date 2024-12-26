class Trie:
    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        trie = self.trie
        for letter in word:
            if letter not in trie:
                trie[letter] = {}
            trie = trie[letter]
        trie["is_word"] = True 

    def search(self, word: str) -> bool:
        trie = self.trie
        for letter in word:
            if letter not in trie:
                return False
            trie = trie[letter]
        return "is_word" in trie

    def startsWith(self, prefix: str) -> bool:
        trie = self.trie
        for letter in prefix:
            if letter not in trie:
                return False
            trie = trie[letter]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)