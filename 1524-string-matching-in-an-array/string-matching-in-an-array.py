class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        # Only lowercase english letters!
        self.getLetterValue = lambda letter: ord(letter) - ord("a") + 1

        # print(f"{self.robinKarp('as', 'mass')=}")
        print(f"{self.robinKarp('hero', 'superhero')=}")
        # return []

        N = len(words)
        res = set()
        for i in range(N):
            for j in range(N):
                # if i != j and words[i] in words[j]:
                if i != j and self.robinKarp(words[i], words[j]):
                    res.add(words[i])
        # print(f"{self.robinKarp('ace', 'ace')=}")
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

        # return hash_to_match
        cur_hash = 0
        power = 0
        print(f"{small_word=}, {big_word=}")
        for i in range(len(small_word) - 1, -1, -1):
            letter = big_word[i]
            val = self.getLetterValue(letter)
            cur_hash += val * pow(26, power)
            power += 1
        
        l = 0
        # length = len(big_word)
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
            
        # >>> def getHash(word):
        # ...     h = 0
        # ...     power = 0
        # ...     for letter in reversed(word):
        # ...             val = (lambda letter: ord(letter) - ord("a") + 1)(letter)
        # ...             h += val * pow(26, power)
        # ...             power += 1
        # ...     return h
        # ... 
        # >>> getHash('ace')
        # 759
        # >>> h = getHash
        # >>> h('ace')
        # 759
        # >>> h('ac')
        # 29
        # >>> h('ace')
        # 759
        # >>> h('cef')
        # 2164
        # >>> length = 3
        # >>> 1 * pow(26, length - 1)
        # 676
        # >>> 759 - 676
        # 83
        # >>> 83 * 26
        # 2158
        # >>> (lambda letter: ord(letter) - ord("a") + 1)('f')
        # 6
        # >>> 