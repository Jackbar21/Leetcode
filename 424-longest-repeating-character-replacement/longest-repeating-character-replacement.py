class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        res = 0
        for letter in set(s):
            res = max(res, self.charReplacementSolver(s, k, letter))
        
        return res
    
    def charReplacementSolver(self, s, k, replace_letter):
        num_to_replace = 0
        res = k
        
        l = 0
        for r in range(len(s)):
            letter = s[r]
            if letter != replace_letter:
                num_to_replace += 1
            
            while l < r and num_to_replace > k:
                if s[l] != replace_letter:
                    num_to_replace -= 1
                l += 1
            
            res = max(res, r - l + 1)
        
        return res