class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        N, M = len(s1), len(s2)
        # if N != M:
        #     return False
        assert N == M
        
        diff_indices = []
        for i in range(N):
            letter1, letter2 = s1[i], s2[i]
            if letter1 == letter2:
                continue
            
            diff_indices.append(i)
            if len(diff_indices) > 2:
                return False # Can only have AT MOST ONE string swap!
        
        count = len(diff_indices)
        assert count in [0,1,2]
        if count == 0:
            return True # No string swaps needed!
        elif count == 1:
            return False # Exactly one character different, so cannot make strings same :(
        else:
            # count == 2, so check if swapping the letters at the two diff. indices will work!
            index1, index2 = diff_indices
            return s1[index1] == s2[index2] and s1[index2] == s2[index1]
