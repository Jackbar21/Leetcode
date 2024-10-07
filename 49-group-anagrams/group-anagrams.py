class Solution:
    def letterToIndex(self, letter):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        return alphabet.find(letter)
    def wordToTuple(self, word):
        res = [0] * 26
        for letter in word:
            index = self.letterToIndex(letter)
            res[index] += 1
        
        return tuple(res)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # {'e': 1, 'a': 1, 't': 1}
        # # abcdefghijklmnopqrstuvwxyz
        # (1, 0, 0, 0, 1, ...)
        d = {}

        for word in strs:
            tuple_word = self.wordToTuple(word)
            if tuple_word in d:
                d[tuple_word].append(word)
            else:
                d[tuple_word] = [word]
        
        return [arr for arr in d.values()]