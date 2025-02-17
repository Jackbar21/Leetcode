class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        self.res = 0

        # Setup "options" tile-to-frequency mappings
        d = {}
        for tile in tiles:
            d[tile] = d.get(tile, 0) + 1

        def backtrack():
            self.res += 1
            for letter, freq in d.items():
                if freq == 0:
                    continue
                
                # Backtrack logic
                d[letter] -= 1
                backtrack()
                d[letter] += 1
        
        # Initial backtrack call
        backtrack()

        # Exclude empty string from results!
        return self.res - 1
