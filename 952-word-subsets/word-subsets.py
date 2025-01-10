class Solution:
    @cache
    def getDictFromWord(self, word):
        d = {}
        for letter in word:
            d[letter] = d.get(letter, 0) + 1
        return d
    
    def isWordSubset(self, small_word, big_word):
        # assert len(small_word) <= len(big_word)
        # l = 0
        # for r in range(len(big_word)):
        #     if small_word[l] == big_word[r]:
        #         l += 1
        #         if l >= len(small_word):
        #             return True
        # return False
        ds, db = self.getDictFromWord(small_word), self.getDictFromWord(big_word)
        for letter, frequency in ds.items():
            if frequency > db.get(letter, 0):
                return False
        return True

    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        

        # Since the letters of each word consists of lowercase English letters, we can compute
        # for each letter in the alphabet, the word in words2 that contains that letter the
        # MOST amount of times. Then, for any word1 in words1, we know that having every word
        # in words2 being a subset of word1 is logically equivalent to whether word1 is a SUPERSET
        # of every word in words2. Hence, we can just check the frequency of each character in
        # word1, and confirm that it is always >= to the word in words2 containing that letter
        # with MAXIMAL frequency. Namely, we leverage the fact that:
        #       word2 subset of word1 for all word2 in words2
        #       <==> word1 a superset of word2 for all words in word2
        d = defaultdict(lambda: float("-inf"))
        for word in words2:
            word_dict = self.getDictFromWord(word)
            for letter, frequency in word_dict.items():
                # if frequency < d.get(letter, float("inf")):
                if frequency > d[letter]:
                    d[letter] = frequency
        
        print(f"{d=}")
        
        # Don't need a hash-set for result, since constraints say all strings in words1 are unique!
        universal_words = []

        for word in words1:
            word_dict = self.getDictFromWord(word)
            is_universal = True
            print(f"{word_dict=}")
            for letter, frequency in d.items():
                # For superset, frequency should be greater-than-or-equal-to!
                if not (word_dict.get(letter, 0) >= frequency):
                # if not (frequency >= d.get(letter, 0)):
                    is_universal = False
                    break
            if is_universal:
                universal_words.append(word)
        
        return universal_words

        # return [
            
        #     for word1 in words2
        # ]
        return list(filter(lambda word1: all(self.isWordSubset(word2, word1) for word2 in words2), words1))

        # Given a list of words 'words', and a word 'w', output a boolean that returns
        # True if every word in words is a subset of w, and otherwise False.

        # Step 1: Build a trie of all the words in words2
        self.trie = {}


        # # Map every word in words2 to a letter-to-frequency dictionary!
        # word_to_dict = {}
        # for word in words2:
        #     if word in word_to_dict:
        #         continue
        #     d = defaultdict(int)
        #     for letter in word:
        #         d[letter] += 1
        #     word_to_dict[word] = d

        # for word in words1:

