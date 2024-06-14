class Solution:
    def isValidArr(self, arr):
        s = set()
        for num in arr:
            if num != "." and num in s:
                return False
            s.add(num)
        return True
    def isValidSquare(self, board, i, j, n=3):
        res = []
        for k1 in range(n):
            for k2 in range(n):
                res.append(board[i+k1][j+k2])
        return self.isValidArr(res)
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if not self.isValidArr(row):
                return False
        
        for col in zip(*board):
            if not self.isValidArr(col):
                return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not self.isValidSquare(board, i, j):
                    return False
        
        return True
        
        
                