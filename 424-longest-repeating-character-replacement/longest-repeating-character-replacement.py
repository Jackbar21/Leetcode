class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        # for letter in set(s):
        #     res = max(res, self.charReplacementSolver(s, k, letter))
        
        # return res
        
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        d = {letter: 0 for letter in alphabet}
        l = 0
        for r in range(len(s)):
            letter = s[r]
            d[letter] = d.get(letter, 0) + 1

            while sum(d.values()) - max(d.values()) > k:
                d[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        
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