class Solution:
    def inBounds(self, i, j):
        return 0 <= i < self.M and 0 <= j < self.N

    def existFromPos(self, i, j):
        board, word = self.board, self.word
        assert self.inBounds(i, j)
        if board[i][j] != word[0]:
            return False
        # elif len(word) == 1:
        #     return True

        queue = collections.deque([(i, j, 0)]) # (x, y, word_index)
        visited = set([(i, j)])
        while len(queue) > 0:
            x, y, word_index = queue.popleft()
            letter = board[x][y]
            # if letter != word[word_index]:
            #     continue
            # elif word_index == len(word) - 1:
            #     return True
            assert letter == word[word_index]
            if word_index == len(word) - 1:
                return True
            
            for dx, dy in self.DIRECTIONS:
                new_x, new_y = x + dx, y + dy
                if not self.inBounds(new_x, new_y):
                    continue
                # Only consider it as a neighbor, if it's not been visited!
                # However, instead of keeping track of a visited set, we can
                # simply just check if it forms the next letter in the desired
                # word :)
                # EDIT: Scrap that, visited set is needed to prevent re-using valid letters!
                if (new_x, new_y) in visited:
                    continue
                
                new_index = word_index + 1
                if word[new_index] == board[new_x][new_y]:
                    queue.append((new_x, new_y, new_index))
                    visited.add((new_x, new_y))


        return False

    def backtrack(self, i, j, word_index, visited):
        letter = self.board[i][j]
        if letter != self.word[word_index]:
            return False
        elif word_index == len(self.word) - 1:
            return True
        
        for di, dj in self.DIRECTIONS:
            x, y = i + di, j + dj
            if ((x, y) not in visited and self.inBounds(x, y)
                and self.board[x][y] == self.word[word_index + 1]
            ):
                visited.add((x, y))
                if self.backtrack(x, y, word_index + 1, visited):
                    return True
                visited.remove((x, y)) # Not discard, since MUST be in there!
        
        return False

        

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.DIRECTIONS = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        self.M, self.N = len(board), len(board[0])
        self.board, self.word = board, word
        for i in range(self.M):
            for j in range(self.N):
                if board[i][j] == word[0] and self.backtrack(i, j, 0, set([(i, j)])):
                    return True
        return False

# A B C E
# S F E S
# A D E E