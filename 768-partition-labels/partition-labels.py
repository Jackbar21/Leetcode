class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # For each letter in s, get the index at which it occurs for the LAST time.
        last = {}
        for i, letter in enumerate(s):
            last[letter] = i
        
        res = []
        l = 0
        min_index = 0
        for r, letter in enumerate(s):
            if min_index < (index := last[letter]):
                min_index = index
            
            # assert r <= min_index
            if r == min_index:
                # Create a new valid section finally!
                res.append(r - l + 1)
                l = r + 1
        
        return res
