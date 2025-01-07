class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        N = len(words)
        res = set()
        for i in range(N):
            for j in range(N):
                word1, word2 = words[i], words[j]
                if i != j and word1 in word2:
                    res.add(word1)
        return list(res)