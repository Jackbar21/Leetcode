class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        # Only lowercase english letters!
        self.getLetterValue = lambda letter: ord(letter) - ord("a") + 1

        N = len(words)
        res = set()
        for i in range(N):
            for j in range(N):
                # if i != j and words[i] in words[j]:
                if i != j and self.robinKarp(words[i], words[j]):
                    res.add(words[i])
        return list(res)
    
    def robinKarp(self, small_word, big_word):
        if len(small_word) > len(big_word):
            return False

        hash_to_match = 0
        power = 0
        for letter in reversed(small_word):
            val = self.getLetterValue(letter)
            hash_to_match += val * pow(26, power)
            power += 1

        cur_hash = 0
        power = 0
        for i in range(len(small_word) - 1, -1, -1):
            letter = big_word[i]
            val = self.getLetterValue(letter)
            cur_hash += val * pow(26, power)
            power += 1
        
        l = 0
        ROBIN_KARP_CONSTANT = pow(26, len(small_word) - 1)
        for r in range(len(small_word), len(big_word)):
            if cur_hash == hash_to_match:
                break
            
            cur_hash -= self.getLetterValue(big_word[l]) * ROBIN_KARP_CONSTANT
            cur_hash *= 26
            cur_hash += self.getLetterValue(big_word[r])
            l += 1 # For next 'rolling hash' iteration
        
        # Since hashes are UNIQUE per string, 
        # due to lowercase-English-letters-only constraint!
        return cur_hash == hash_to_match
