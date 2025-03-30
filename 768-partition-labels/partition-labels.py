class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # For each letter in s, get the index at which it occurs for the LAST time.
        last = {}
        for i, letter in enumerate(s):
            last[letter] = i
        
        res = []
        l = 0
        # min_index = last[s[0]]
        min_index = float("-inf")
        for r, letter in enumerate(s):
            if min_index < last[letter]:
                min_index = last[letter]
            
            assert r <= min_index
            if r == min_index:
                # Create a new valid section finally!
                # res.append((l, r))
                res.append(r - l + 1)
                l = r + 1
                # min_index = float("-inf")
        
        return res
            


            
        
        print(f"{res=}")
        print(f"result={[s[l:r+1] for (l,r) in res]}")
        print(f"length={[r - l + 1 for (l,r) in res]}")
