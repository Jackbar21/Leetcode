class Solution:
    def __init__(self):
        self.PREFIX_COUNT_SYMBOL = "."
        self.trie = {} # '.' --> frequency of prefix

    def addWord(self, word):
        trie, PREFIX_COUNT_SYMBOL = self.trie, self.PREFIX_COUNT_SYMBOL
        for letter in word:
            if letter not in trie:
                trie[letter] = { PREFIX_COUNT_SYMBOL: 0 }
            trie = trie[letter]
            trie[PREFIX_COUNT_SYMBOL] += 1

    def prefixCount(self, words: List[str], pref: str) -> int:
        # Add every word into the trie, as well as 'pref' so that the prefix
        # is guaranteed to exist at least once in the trie. Since we're including
        # pref in the trie, we will return the final result subtracted by one.
        self.addWord(pref)
        for word in words:
            self.addWord(word)

        # Now, traverse the trie to get the frequency count for 'pref'. Remember to subtract
        # the result by one, since we added pref to the trie as well (to guarantee that it
        # exists in the trie!)
        trie = self.trie
        for letter in pref:
            trie = trie[letter]
        return trie[self.PREFIX_COUNT_SYMBOL] - 1
