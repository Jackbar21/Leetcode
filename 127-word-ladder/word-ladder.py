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
        return list(self.getSimilarWordsHelper(word, 0, self.trie, 1))

    def getSimilarWordsHelper(self, word, index, trie, can_change):
        if index == len(word):
            if self.END_WORD in trie:
                yield trie[self.END_WORD]
            return

        word_letter = word[index]
        if word_letter in trie:
            yield from self.getSimilarWordsHelper(word, index + 1, trie[word_letter], can_change)

        if can_change > 0:
            for letter in self.ALPHABET:
                if letter not in trie or letter == word_letter:
                    continue
                yield from self.getSimilarWordsHelper(word, index + 1, trie[letter], can_change - 1)

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        self.trie = {}
        self.END_WORD = "."
        self.ALPHABET = "abcdefghijklmnopqrstuvwxyz"
        self.addWord(beginWord)
        for word in wordList:
            self.addWord(word)

        wordList.append(beginWord)
        wordList.sort()
        N = len(wordList)
        WORD_LENGTH = len(beginWord)

        queue = collections.deque([(1, beginWord)]) # (cost, word)
        # available_words = set(wordList) # i.e. unvisited
        # if endWord not in available_words:
        #     return 0
        visited = set([beginWord])
        while len(queue) > 0:
            cost, word = queue.popleft()
            if word == endWord:
                return cost
            
            # used_words = set()
            # for word in available_words:
            #     diff_count = 0
            #     for index in range(WORD_LENGTH):
            #         diff_count += node[index] != word[index]
            #         if diff_count > 1:
            #             break
                
            #     if diff_count == 1:
            #         used_words.add(word)
            #         queue.append((cost + 1, word))
            for neigh in self.getSimilarWords(word):
                if neigh not in visited:
                    queue.append((cost + 1, neigh))
                    visited.add(neigh)
        
        return 0

        # Original Solution
        adj_list = {word: [] for word in wordList}
        for i, word_i in enumerate(wordList):
            for j in range(i + 1, len(wordList)):
                word_j = wordList[j]
                diff_count = 0
                
                # assert len(word_i) == len(word_j) == WORD_LENGTH
                for index in range(WORD_LENGTH):
                    diff_count += word_i[index] != word_j[index]
                    if diff_count > 1:
                        break
                
                if diff_count == 1:
                    adj_list[word_i].append(word_j)
                    adj_list[word_j].append(word_i)
        
        queue = collections.deque([(1, beginWord)]) # (cost, word)
        visited = set()
        while len(queue) > 0:
            cost, node = queue.popleft()
            if node == endWord:
                return cost

            for neigh in adj_list[node]:
                if neigh not in visited:
                    queue.append((cost + 1, neigh))
                    visited.add(neigh)

        # No such sequence exists!
        return 0

