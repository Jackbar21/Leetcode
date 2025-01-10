class Solution:
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
        def getDictFromWord(word):
            d = defaultdict(int)
            for letter in word:
                d[letter] += 1
            return d

        d = defaultdict(int)
        for word in words2:
            word_dict = getDictFromWord(word)
            for letter, frequency in word_dict.items():
                if frequency > d[letter]:
                    d[letter] = frequency
        LETTER_FREQUENCY_PAIRS = d.items()
        
        # Don't need a hash-set for result, since constraints say all strings in words1 are unique!
        universal_words = []

        for word in words1:
            word_dict = getDictFromWord(word)
            is_universal = True
            for letter, frequency in LETTER_FREQUENCY_PAIRS:
                # For superset, frequency should be greater-than-or-equal-to!
                if word_dict[letter] < frequency:
                    is_universal = False
                    break
            if is_universal:
                universal_words.append(word)

        return universal_words
