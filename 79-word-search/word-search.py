class Solution:
    def inBounds(self, i, j):
        return 0 <= i < self.M and 0 <= j < self.N

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
                if self.backtrack(i, j, 0, set([(i, j)])):
                    return True
        return False
