class Spreadsheet:

    def __init__(self, rows: int):
        self.alphabet = set("abcdefghijklmnopqrstuvwxyz".upper())
        self.d = {letter: defaultdict(int) for letter in self.alphabet}

    def setCell(self, cell: str, value: int) -> None:
        letter = cell[0]
        number = int(cell[1:])
        self.d[letter][number] = value

    def resetCell(self, cell: str) -> None:
        letter = cell[0]
        number = int(cell[1:])
        self.d[letter][number] = 0
        
    def getValue(self, formula: str) -> int:
        assert formula[0] == "="

        res = 0
        for val in (formula[1:]).split("+"):
            if val[0] in self.alphabet:
                letter = val[0]
                number = int(val[1:])
                res += self.d[letter][number]
            else:
                res += int(val)
        
        return res

# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)