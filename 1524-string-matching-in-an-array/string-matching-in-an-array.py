class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = set()
        for i, word_i in enumerate(words):
            for j, word_j in enumerate(words):
                if i != j and word_i in word_j:
                    res.add(word_i)
        return list(res)