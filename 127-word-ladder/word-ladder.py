class Solution:
    def addWord(self, word):
        trie = self.trie
        for letter in word:
            if letter not in trie:
                trie[letter] = {}
            trie = trie[letter]
        trie[self.END_WORD] = word
    
    def isPrefix(self, word):
        trie = self.trie
        for letter in word:
            if letter not in trie:
                return False
            trie = trie[letter]
        return True
    
    def isWord(self, word):
        trie = self.trie
        for letter in word:
            if letter not in trie:
                return False
            trie = trie[letter]
        return self.END_WORD in trie and trie[self.END_WORD] == word
    
    def getSimilarWords(self, word):
        self.res = []
        self.getSimilarWordsHelper(word, 0, self.trie, 1)
        return self.res

    def getSimilarWordsHelper(self, word, index, trie, can_change):
        if index == len(word):
            if self.END_WORD in trie:
                self.res.append(trie[self.END_WORD])
            return

        word_letter = word[index]
        if word_letter in trie:
            self.getSimilarWordsHelper(word, index + 1, trie[word_letter], can_change)

        if can_change > 0:
            for letter in trie:
                if letter != word_letter:
                    self.getSimilarWordsHelper(word, index + 1, trie[letter], can_change - 1)

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        self.trie = {}
        self.END_WORD = "."
        for word in wordList:
            self.addWord(word)

        queue = collections.deque([(1, beginWord)]) # (cost, word)
        visited = set([beginWord])
        while len(queue) > 0:
            cost, word = queue.popleft()
            if word == endWord:
                return cost

            for neigh in self.getSimilarWords(word):
                if neigh not in visited:
                    queue.append((cost + 1, neigh))
                    visited.add(neigh)

        # No solution
        return 0
