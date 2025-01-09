class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        # return self.prefixCountTrie(words, pref)
        # return sum(word.startswith(pref) for word in words)
        res = 0
        for word in words:
            if word.startswith(pref):
                res += 1
        return res

    def addWord(self, word):
        trie, PREFIX_COUNT_SYMBOL = self.trie, self.PREFIX_COUNT_SYMBOL
        for letter in word:
            if letter not in trie:
                trie[letter] = { PREFIX_COUNT_SYMBOL: 0 }
            trie = trie[letter]
            trie[PREFIX_COUNT_SYMBOL] += 1

    def prefixCountTrie(self, words: List[str], pref: str) -> int:
        # Initial Trie setup!
        self.PREFIX_COUNT_SYMBOL = "."
        self.trie = {} # '.' --> frequency of prefix

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
