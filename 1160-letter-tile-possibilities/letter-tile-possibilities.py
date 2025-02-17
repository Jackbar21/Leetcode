class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        self.res = 0

        d = {}
        for tile in tiles:
            d[tile] = d.get(tile, 0) + 1

        # arr = []
        def backtrack():
            self.res += 1
            for letter, freq in d.items():
                # assert freq >= 0
                if freq == 0:
                    continue
                
                # arr.append(letter)
                d[letter] -= 1
                backtrack()
                # assert arr.pop() == letter
                d[letter] += 1
        
        backtrack()
        return self.res - 1 # Exclude empty string from results!
