class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        N, M = len(s1), len(s2)
        if N != M:
            return False
        
        diff_indices = []
        for i in range(N):
            letter1, letter2 = s1[i], s2[i]
            if letter1 == letter2:
                continue
            
            diff_indices.append(i)
            if len(diff_indices) > 2:
                return False
        
        count = len(diff_indices)
        # No string swaps needed!
        if count == 0:
            return True 

        # Check if swapping the letters at the two diff. indices will work!
        if count == 2:
            i, j = diff_indices
            return s1[i] == s2[j] and s1[j] == s2[i]

        # Need exactly 2 (if not 0) characters different to make swap work!
        return False