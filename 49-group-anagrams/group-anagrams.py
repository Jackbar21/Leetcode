class Solution:
    def wordToTuple(self, word):
        res = [0] * 26
        for letter in word:
            # ord('a') == 97
            res[ord(letter) - 97] += 1
        return tuple(res)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for word in strs:
            tuple_word = self.wordToTuple(word)
            if tuple_word in d:
                d[tuple_word].append(word)
            else:
                d[tuple_word] = [word]

        return d.values()