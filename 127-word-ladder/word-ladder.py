class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if (endWord not in wordList 
            or len(beginWord) != len(endWord) 
            or beginWord == endWord
        ):
            return 0

        queue = collections.deque([(beginWord, 0)])
        visited = set([beginWord])
        wordList = set(wordList)

        while len(queue) > 0:
            word, path_len = queue.popleft()

            if len(word) != len(beginWord):
                continue
            
            if word == endWord:
                return path_len + 1

            for i in range(len(beginWord)):
                for letter in 'qwertyuiopasdfghjklzxcvbnm':
                    new_word = word[:i] + letter + word[i+1:]
                    if letter == word[i] or new_word not in wordList:
                        continue
                    if new_word not in visited:
                        queue.append((new_word, path_len + 1))
                        visited.add(new_word)

        return 0