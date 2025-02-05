class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        
        N = len(s1)
        diff_indices = []
        for i in range(N):
            letter1, letter2 = s1[i], s2[i]
            if letter1 == letter2:
                continue
            
            diff_indices.append(i)
            if len(diff_indices) > 2:
                return False
        
        count = len(diff_indices)
        assert count in [0,1,2]
        if count == 0:
            return True
        if count == 1:
            return False
        
        assert count == 2
        index1, index2 = diff_indices
        return s1[index1] == s2[index2] and s1[index2] == s2[index1]
