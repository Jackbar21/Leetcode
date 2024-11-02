class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        # letter-to-frequency mappings for s1 & s2, respectively
        d1, d2 = defaultdict(int), defaultdict(int)
        for letter in s1:
            d1[letter] += 1

        for i in range(len(s1)):
            d2[s2[i]] += 1

        l = 0
        for r in range(len(s1), len(s2)):
            # Return true if permutation of one another
            if d1 == d2:
                return True
            
            # Update window (fixed-size)
            d2[s2[l]] -= 1
            if d2[s2[l]] == 0:
                del d2[s2[l]]
            d2[s2[r]] += 1
            l += 1
        
        return d1 == d2
