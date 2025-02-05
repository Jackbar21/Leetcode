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
                break
        
        count = len(diff_indices)
        # No string swaps needed!
        if count == 0:
            return True 

        # Check if swapping the letters at the two diff. indices will work!
        if count == 2:
            index1, index2 = diff_indices
            return s1[index1] == s2[index2] and s1[index2] == s2[index1]

        # Need exactly 2 (if not 0) characters different to make swap work!
        return False