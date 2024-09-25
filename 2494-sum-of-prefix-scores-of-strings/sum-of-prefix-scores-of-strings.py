class Solution:
    def __init__(self):
        self.trie = {} # "pc": INT, for prefix counts
    def insertWord(self, word):
        trie = self.trie
        for letter in word:
            if letter not in trie:
                trie[letter] = {"pc": 0}

            trie = trie[letter]
            trie["pc"] += 1
    def getPrefixSum(self, word):
        res = 0
        trie = self.trie
        for letter in word:
            if letter not in trie:
                break
            trie = trie[letter]
            assert "pc" in trie
            res += trie["pc"]
        return res
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        for word in words:
            self.insertWord(word)
        return map(self.getPrefixSum, words)