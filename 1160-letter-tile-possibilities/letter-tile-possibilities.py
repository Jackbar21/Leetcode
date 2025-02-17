class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        res = set()

        d = {}
        for tile in tiles:
            d[tile] = d.get(tile, 0) + 1

        arr = []
        def backtrack():
            res.add("".join(arr))
            for letter, freq in d.items():
                assert freq >= 0
                if freq == 0:
                    continue
                
                arr.append(letter)
                d[letter] -= 1
                backtrack()
                assert arr.pop() == letter
                d[letter] += 1
        
        backtrack()
        res.discard("")
        # print(f"{res=}")
        return len(res)
