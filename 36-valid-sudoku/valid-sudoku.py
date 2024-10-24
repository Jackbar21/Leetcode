class Solution:
    def isValidRow(self, board, row_index):
        row = board[row_index]
        seen = set()
        for num in row:
            if num != "." and num in seen:
                return False
            seen.add(num)
        return True
    
    def isValidColumn(self, board, col_index):
        seen = set()
        for row in board:
            num = row[col_index]
            if num != "." and num in seen:
                return False
            seen.add(num)
        return True

    def isValidBox(self, board, row_index, col_index):
        seen = set()
        for dr in range(3):
            for dc in range(3):
                num = board[row_index + dr][col_index + dc]
                if num != "." and num in seen:
                    return False
                seen.add(num)
        return True
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Step 1: Check all the rows (9 rows in total!)
        # for row_index in range(9):
        #     if not self.isValidRow(board, row_index):
        #         return False

        # # Step 2: Check all the columns (9 columns in total!)
        # for col_index in range(9):
        #     if not self.isValidColumn(board, col_index):
        #         return False

        for index in range(9):
            if not self.isValidRow(board, index) or not self.isValidColumn(board, index):
                return False

        # Step 3: Check all the 3 x 3 sub-boxes (9 boxes in total!)
        for row_index in [0, 3, 6]:
            for col_index in [0, 3, 6]:
                if not self.isValidBox(board, row_index, col_index):
                    return False

        return True