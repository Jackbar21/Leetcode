class Solution:
    def addWord(self, word):
        trie = self.trie
        for letter in word:
            if letter not in trie:
                trie[letter] = {}
            trie = trie[letter]
        trie[self.END_WORD] = word
    
    def isWord(self, word):
        trie = self.trie
        for letter in word:
            if letter not in trie:
                return False
            trie = trie[letter]
        return self.END_WORD in trie
    
    def isPrefix(self, word):
        trie = self.trie
        for letter in word:
            if letter not in trie:
                return False
            trie = trie[letter]
        return True

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.END_WORD = "."
        self.trie = {}

        for word in words:
            self.addWord(word)
        
        # print(f"{self.trie=}")
        # for word in ["oath", "oat", "oathyum"]:
        #     print(f"{word=}, {self.isWord(word)=}, {self.isPrefix(word)=}")

        self.DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        self.board = board
        self.res = set()
        M, N = len(board), len(board[0])
        self.inBounds = lambda i, j: 0 <= i < M and 0 <= j < N
        for i in range(M):
            for j in range(N):
                # self.bfs(i, j)
                # self.bfs_trie(i, j)
                letter = board[i][j]
                if letter not in self.trie:
                    continue
                self.dp(i, j, self.trie[letter], set([(i, j)]))
        return list(self.res)
    
    def dp(self, i, j, trie, visited):
        # if not self.inBounds(i, j):
        #     return
        
        # letter = self.board[i][j]
        # if letter not in trie:
        #     return
        
        # trie = trie[letter]
        if self.END_WORD in trie:
            self.res.add(trie[self.END_WORD])
        
        for di, dj in self.DIRECTIONS:
            neigh_i, neigh_j = i + di, j + dj
            if not self.inBounds(neigh_i, neigh_j):
                continue
            if (neigh_i, neigh_j) in visited:
                continue
            # visited.add((neigh_i, neigh_j))

            letter = self.board[neigh_i][neigh_j]
            if letter in trie:
                visited.add((neigh_i, neigh_j))
                self.dp(neigh_i, neigh_j, trie[letter], visited)
                visited.remove((neigh_i, neigh_j))

    
    def bfs_trie(self, i, j):
        letter = self.board[i][j]
        if letter not in self.trie:
            return
        queue = collections.deque([(i, j, self.trie[letter])])
        visited = set([(i, j)])
        while len(queue) > 0:
            i, j, trie = queue.popleft()
            if self.END_WORD in trie:
                self.res.add(trie[self.END_WORD])
            
            for di, dj in self.DIRECTIONS:
                neigh_i, neigh_j = i + di, j + dj
                if (neigh_i, neigh_j) in visited:
                    continue
                if not self.inBounds(neigh_i, neigh_j):
                    continue
                
                neigh_letter = self.board[neigh_i][neigh_j]
                if neigh_letter in trie:
                    queue.append((neigh_i, neigh_j, trie[neigh_letter]))
                    visited.add((neigh_i, neigh_j))


    
    def bfs(self, i, j):
        letter = self.board[i][j]
        queue = collections.deque([(i, j, [letter])])
        visited = set([(i, j)])
        while len(queue) > 0:
            i, j, letters = queue.popleft()
            # if not self.isPrefix(letters):
            #     continue
            print(f"{''.join(letters)=}")
            if self.isWord(letters):
                self.res.add("".join(letters))
            
            for di, dj in self.DIRECTIONS:
                neigh_i, neigh_j = i + di, j + dj
                if not self.inBounds(neigh_i, neigh_j) or (neigh_i, neigh_j) in visited:
                    continue
                visited.add((neigh_i, neigh_j))
                
                neigh_letter = self.board[neigh_i][neigh_j]
                neigh_letters = letters + [neigh_letter] # TODO: Inefficient!
                # if not self.isPrefix(neigh_letters):
                #     continue

                queue.append((neigh_i, neigh_j, neigh_letters))


            
# o a a n
# e t a e
# i h k r
# i f l v   