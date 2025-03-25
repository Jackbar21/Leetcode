class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.append(beginWord)
        N = len(wordList)
        WORD_LENGTH = len(beginWord)

        adj_list = {word: [] for word in wordList}
        for i, word_i in enumerate(wordList):
            for j in range(i + 1, len(wordList)):
                word_j = wordList[j]
                diff_count = 0
                
                # assert len(word_i) == len(word_j) == WORD_LENGTH
                for index in range(WORD_LENGTH - 1, -1, -1):
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

