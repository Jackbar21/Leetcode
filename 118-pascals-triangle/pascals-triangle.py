class Solution:
    @cache
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        
        rows = self.generate(numRows - 1)
        last_row = rows[-1]
        row = [1]
        for i in range(1, len(last_row)):
            row.append(last_row[i - 1] + last_row[i])
        row.append(1)
        rows.append(row)
        return rows